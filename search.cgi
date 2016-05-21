#!/usr/bin/perl

use strict;
use CGI;

require 'config.cgi';
require 'utility.cgi';

my $q = new CGI;

my $logfile = &LogFile();
#my $location = &Location();
#my $maxlog = &MaxLog();

my $mode = $q->param('mode');
my $word = $q->param('word');

#print "Content-type: text/html\n\n";
#print $mode;
#exit(0);

if($mode eq 'Form'){&Form();}
if($mode eq 'Search'){&Search($word);}


sub Form {
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
<input type=button value="戻る" onClick="parent.location.href = './'" />
</form><br /><br />
<form action="./search.cgi" method=post><br />
<input type="hidden" name="mode" value="Search" />
<input type="text" name="word" size="24" />
<input type="submit" value=" 検索 " />
</form>
</body>
</html>
EOM

}

sub Search {
	my($no, $date, $name, $email, $url, $subject, $mess, $pass);
	my $i=0;
	
	if($word eq ""){
		&PrintError("キーワードを入力してください");
		exit(0);
	}
	
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
<input type=button value="戻る" onClick="parent.location.href = './'" />
</form><br /><br />
EOM

open(IN,"$logfile") || print "Open Error: $logfile";
while(<IN>){
	($no, $date, $name, $email, $url, $subject, $mess, $pass) = split(/<>/);
	if(($date =~ /$word/) || ($name =~ /$word/) || ($email =~ /$word/) || 
	   ($url =~ /$word/) || ($subject =~ /$word/) || ($mess =~ /$word/)){
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
		
		$i++;
	} 
}

close(IN);

if($i == 0){
	print "検索結果：0件";
}
print "</body></html>";

}

exit(0);
