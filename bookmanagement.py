import bottle
import lmdb
import json


env = lmdb.Environment("./dbbook")


def get_id(txn):
    cur = txn.cursor()
    ite = cur.iterprev()
    try:
        k, v = next(ite)
        last_id = int(k.decode("utf8"))
    except StopIteration:
        last_id = 0
    id = last_id + 1
    return "{:08d}".format(id)


def lend(txn):
    id = bottle.request.params.id
    print(id)
    d = txn.get(id.encode("utf-8"))
    data = json.loads(d)
    print(data)
    ls = data["lending_status"]
    print(ls)
    if ls == "0":
        data["lending_status"] = "1"
    else:
        data["lending_status"] = "0"
    print(data)
    txn.put(id.encode("utf-8"), json.dumps(data).encode("utf8"),
            overwrite=True)
    return data


@bottle.route("/")
def root():
    return bottle.static_file("entry.html", root="./static")


@bottle.post("/submit")
@bottle.view("submit")
def submit():
    with env.begin(write=True) as txn:
        id = get_id(txn)
        title = bottle.request.params.title
        author = bottle.request.params.author
        publisher = bottle.request.params.publisher
        date = bottle.request.params.date
        lending_status = "0"
        data = {"title": title, "author": author,
                "publisher": publisher, "date": date, "id": id,
                "lending_status": lending_status
                }
        txn.put(id.encode("utf8"), json.dumps(data).encode("utf8"))
    return data


@bottle.route("/list")
@bottle.view("list")
def list():
    data = []
    with env.begin() as txn:
        cur = txn.cursor()
        for k, v in cur:
            d = json.loads(v.decode("utf8"))
            ls = d["lending_status"]
            print(ls)
            if ls == "0":
                d["lending_status"] = "在庫"
            else:
                d["lending_status"] = "貸出中"
            data.append(d)
    for d in data:
        print(d)
    return {"data": data}


@bottle.get("/delete")
@bottle.view("delete")
def delete():
    id = bottle.request.params.id
    print(id)
    with env.begin(write=True) as txn:
        d = txn.get(id.encode("utf-8"))
        data = json.loads(d)
        txn.delete(id.encode("utf-8"))
    return data


@bottle.get("/detail")
@bottle.view("detail")
def detail():
    id = bottle.request.params.id
    print(id)
    with env.begin() as txn:
        d = txn.get(id.encode("utf-8"))
        data = json.loads(d)
    print(data)
    ls = data["lending_status"]
    if ls == "0":
        status = "在庫"
        motion = "借りる"
    else:
        status = "貸出中"
        motion = "返却"
    data["status"] = status
    data["motion"] = motion
    return data


@bottle.get("/lending")
@bottle.view("lending")
def lending():
    with env.begin(write=True) as txn:
        data = lend(txn)
    ls = data["lending_status"]
    if ls == "0":
        text = "返却し"
    else:
        text = "借り"
    data["text"] = text
    print(data)

    return data


bottle.run()
