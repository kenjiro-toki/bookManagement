<!DOCTYPE HTML> <html lang="ja"> <head></head> <body> <h2>本一覧</h2>
<table border="solid">
<thead> <td>タイトル</td><td>著者</td><td>出版社</td>
<td>購入日</td><td>貸出状況</td>
</thead>
<tbody>
%for d in data:
<tr>
<td>{{d["title"]}}</td> <td>{{d["author"]}}</td> <td>{{d["publisher"]}}</td> <td>{{d["date"]}}</td> <td>{{d["lending_status"]}}</td>
<td><form method="GET" action="detail"> <input type="submit" value="詳細"> <input type="hidden" name="id" value={{d["id"]}} /> </form></td>
<td><form method="GET" action="delete"> <input type="submit" value="削除"> <input type="hidden" name="id" value={{d["id"]}} /> </form></td>
</tr>
%end
</tbody>
</table>
<p><a href="/">新規登録</a></p>
</body>
</html>