#!/usr/bin/perl

use strict;

require 'config.cgi';

#if ($ENV{'REQUEST_METHOD'} eq "POST"){
#	exit(0);
#}

my $home  = &Home();
my $title = &Title();
my $logfile = &LogFile();
my $page = &Page();

my($no, $date, $name, $email, $url, $subject, $mess, $pass);
my($buf, $p, $pcount);
my($i, $j);
my($div);
my(@index);

	print "Content-type: text/html\n\n";
	print <<"EOM";
<?xml version="1.0" encoding="EUC-JP"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=EUC-JP" />
<link rel="stylesheet" href="./css/cbbs_perl.css" type="text/css" charset="EUC_JP" />
<title>cbbs_perl</title>
</head>
<body>
<form>
<input type=button value="HOME" onClick="parent.location.href = '$home'" />
<input type=button value="書き込む" onClick="parent.location.href = './form.cgi'" />
<input type=button value="検索" onClick="parent.location.href = './search.cgi?mode=Form'" />
</form>
<h1>$title</h1><br />
<br />
EOM

#$buf = $ENV{'QUERY_STRING'};
print "$buf<br />\n";


open(IN,"$logfile") || print "Open Error: $logfile";
while(<IN>){}
$pcount = $.;

seek(IN, 0, 0);

$div = $pcount / $page;
#$div = int($div);

($i,$p) = split(/=/,$ENV{'QUERY_STRING'});
$p = int($p);

for ($i=0; $i < $div; $i++){
	if($i == ($p-1)){
		$index[$i] = sprintf("[%d]/", $i+1);
	}else{
		$index[$i] = sprintf("<a href=\"./?p=%d\">%d/</a>",$i+1, $i+1);
	}
}
#if($p == $div){
#	push(@index, sprintf("<a href=\"./?p=%d\"><</a>",$p-1));
#}elsif(($p ==1) || ($p == "")){
#	push(@index, "<a href=\"./$p\">></a>");
#}elsif($div == 1){
#
#}else{
#	push(@index, sprintf("<a href=\"./?p=%d\"><</a>&nbsp;<a href=\"./?p=%d\">></a>",$p-1, $p+1));
#}

&PrintIndex(@index);
#for ($i=0; $i < $div; $i++){
#	print "$index[$i]";
#}
print "\n";



if ($p > 1){
	$p--;
	$j = $p * $page;
	for ($i=0; $i < $j; $i++) {
		$buf = <IN>;
	}
}	

for ($i=0; $i < $page; $i++){
	$buf = <IN>;
	if ($buf == ""){
		last;
	}
	($no, $date, $name, $email, $url, $subject, $mess, $pass) = split(/<>/, $buf);
	print "<hr />";
	print "<p class=\"black\">";
	print "No：$no&nbsp;&nbsp;";
	print "題名：$subject&nbsp;&nbsp;";
	print "名前：$name&nbsp;&nbsp;";
	print "<a href=\"mailto:$email\"><img src=\"./img/mail.gif\" border=\"0\" /></a>&nbsp;&nbsp;";
	print "<a href=\"http://$url\"><img src=\"./img/home.gif\" border=\"0\" /></a>&nbsp;&nbsp;";
	print "日付：$date";
	print "<br /><br />";
	print "</p>";
	print "$mess<br />\n";
}

close(IN);

print "<hr />\n";
&PrintIndex(@index);

#for ($i=0; $i < $div; $i++){
#	print "$index[$i]";
#}
print "<br /><br />\n";
	print <<"EOM";
<form action="./edit.cgi" method=post><br />
<table border="0" cellpadding="2" cellspacing="2">
<tr>
<td bgcolor="#f9eff1">
<input type="hidden" name="mode" value="Delete">
<tt>記事番号</tt>

</td>
<td>
<input type="text" name="no" size="24">
</td>
</tr>
<tr>
<td bgcolor="#f9eff1">
<tt>パスワード</tt>
</td>
<td>
<input type="password" name="pass" size="24" maxlength="20">&nbsp;<input type="submit" value=" 削除 " />
</td>
</tr>
</table>
</form>
EOM
print "</body>\n";
print "</html>\n";

sub PrintIndex {
	my(@index) = @_;
	my $i;
	my $j = @index;
	
	for ($i=0; $i < $j; $i++){
		print "$index[$i]";
	}
}
exit(0);


