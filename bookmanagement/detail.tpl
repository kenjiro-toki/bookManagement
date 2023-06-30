<!DOCTYPE HTML>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>詳細</title>
</head>
<body>
<ul>
詳細
<li>タイトル：{{title}}</li>
<li>著者：{{author}}</li>
<li>出版社：{{publisher}}</li>
<li>購入日：{{date}}</li>
<li>状態：{{status}}<form method="GET" action="lending"> <input type="submit" value={{motion}}> <input type="hidden" name="id" value={{id}} /> </form></li>
</ul>
<p><a href="/">新規登録</a></p>
<p><a href="/list">本一覧</a></p>
</html>