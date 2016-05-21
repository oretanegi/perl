#!/usr/bin/perl

use strict;

#if ($ENV{'REQUEST_METHOD'} eq "GET"){
#	exit(0);
#}
	print "Content-type: text/html\n\n";
	print <<"EOM";
<?xml version="1.0" encoding="EUC-JP"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=EUC-JP" />
<title>cbbs_perl</title>
</head>
<body>

<form>
<input type=button value="戻る" onClick="parent.location.href = './'" />
</form><br /><br />
<form action="./edit.cgi" method=post><br />
<table border="0" cellpadding="2" cellspacing="2">
<tr>
<td bgcolor="#f9eff1">
<input type="hidden" name="mode" value="New">
<tt>お名前</tt>

</td>
<td>
<input type="text" name="name" size="24">
</td>
</tr>
<tr>
<td bgcolor="#f9eff1">
<tt>メール</tt>
</td>
<td>
<input type="text" name="email" size="30">
</td>
</tr>
<tr>
<td bgcolor="#f9eff1">
<tt>題名</tt>

</td>
<td>
<input type="text" name="subject" size="30">
</td>
</tr>
<tr>
<td bgcolor="#f9eff1">
本文
</td>
<td>
<textarea name="mess" rows="5" cols="82"></textarea>
</td>
</tr>
<tr>
<td bgcolor="#f9eff1">
<tt>http://</tt>

</td>
<td>
<input type="text" name="url" size="30">
</td>
</tr>
<tr>
<td bgcolor="#f9eff1">
<tt>パスワード</tt>
</td>
<td>
<input type="password" name="pass" size="8" maxlength="20">
</td>
</tr>
<tr>
<td>
</td>

<td>
<input type="submit" value=" 投稿 " /><input type="reset" value="消す" />
</td>
</tr>
</table>
</form>
EOM

print "</body></html>";

