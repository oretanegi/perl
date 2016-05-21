#!/usr/bin/perl

use strict;


sub GetDate {
	my($min,$hour,$mday,$mon,$year,$wday) = (localtime(time))[1..6];
	my(@wk) = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
	my($date) = sprintf("%04d/%02d/%02d(%s) %02d:%02d",
	$year+1900,$mon+1,$mday,$wk[$wday],$hour,$min);
	
	return $date;
}

sub PrintError {
	my $mess = $_[0];
	
	print "Content-type: text/html\n\n";
	print <<"EOM";
<?xml version="1.0" encoding="EUC-JP"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=EUC-JP" />
<link rel="stylesheet" href="./css/cbbs_perl.css" type="text/css" charset="EUC_JP" />
<title>$mess</title>
</head>
<body>
EOM

print $mess;
print "</body></html>";


}
1;
