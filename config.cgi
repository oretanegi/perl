#!/usr/bin/perl

#PerlにはC言語のdefine文のようなものはないのかな・・・

use strict;

sub Home     { return 'http://.com';}
sub Title    { return 'cbbs_perl(beta version 1)';}
sub LogFile  { return './log/log.cgi';}
sub Location { return 'http:///cgi-bin/cbbs_perl/';}
sub MaxLog   { return 100;}
sub Page     { return 10;}
sub Pass     { return 'pass';}


1;


