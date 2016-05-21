#!/usr/bin/perl

use strict;
use CGI;

require 'config.cgi';
require 'utility.cgi';

my $q = new CGI;

my $logfile = &LogFile();
my $location = &Location();
my $maxlog = &MaxLog();

my $mode = $q->param('mode');

#print "Content-type: text/html\n\n";
#print $mode;
#exit(0);

if($mode eq 'New'){&New();}
if($mode eq 'Delete'){&Delete();}


sub New {
	my($pcount, $i, $j);
	my @log;

	my($no, $date, $name, $email, $url, $subject, $mess, $pass);
	my($tno, $tdate, $tname, $temail, $turl, $tsubject, $tmess, $tpass);


	
	$name = $q->param('name');
	$email = $q->param('email');
	$subject = $q->param('subject');
	$mess = $q->param('mess');
	$url = $q->param('url');
	$pass = $q->param('pass');
	
	
	$name =~ s/&/&amp;/g;
	$name =~ s/</&lt;/g;
	$name =~ s/>/&gt;/g;
	$name =~ s/"/&quot;/g; #"
	$name =~ s/\r\n/<br \/>/g;
	$name =~ s/\r/<br \/>/g;
	$name =~ s/\n/<br \/>/g;
	
	
	$email =~ s/&/&amp;/g;
	$email =~ s/</&lt;/g;
	$email =~ s/>/&gt;/g;
	$email =~ s/"/&quot;/g; #"
	$email =~ s/\r\n/<br \/>/g;
	$email =~ s/\r/<br \/>/g;
	$email =~ s/\n/<br \/>/g;
	
	
	$subject =~ s/&/&amp;/g;
	$subject =~ s/</&lt;/g;
	$subject =~ s/>/&gt;/g;
	$subject =~ s/"/&quot;/g; #"
	$subject =~ s/\r\n/<br \/>/g;
	$subject =~ s/\r/<br \/>/g;
	$subject =~ s/\n/<br \/>/g;
	
	
	$mess =~ s/&/&amp;/g;
	$mess =~ s/</&lt;/g;
	$mess =~ s/>/&gt;/g;
	$mess =~ s/"/&quot;/g; #"
	$mess =~ s/\r\n/<br \/>/g;
	$mess =~ s/\r/<br \/>/g;
	$mess =~ s/\n/<br \/>/g;
	
	
	$url =~ s/&/&amp;/g;
	$url =~ s/</&lt;/g;
	$url =~ s/>/&gt;/g;
	$url =~ s/"/&quot;/g; #"
	$url =~ s/\r\n/<br \/>/g;
	$url =~ s/\r/<br \/>/g;
	$url =~ s/\n/<br \/>/g;
	
	
	$pass =~ s/&/&amp;/g;
	$pass =~ s/</&lt;/g;
	$pass =~ s/>/&gt;/g;
	$pass =~ s/"/&quot;/g; #"
	$pass =~ s/\r\n/<br \/>/g;
	$pass =~ s/\r/<br \/>/g;
	$pass =~ s/\n/<br \/>/g;
	

	
	if($mess eq ""){
		&PrintError("本文がありません");
		exit(0);
	}

#if ($ENV{'REQUEST_METHOD'} eq "GET"){
#	exit(0);
#}



#print "Content-type: text/html\n\n";
#print "投稿データ ";
#print "$name ";
#print "$email ";
#print "$subject ";
#print "$mess ";
#print "$url ";
#print "$pass ";

	open(IN,"+< $logfile") || print "Open Error: $logfile";
	flock(IN, 2);
	while(<IN>){}
	$pcount = $.;
	seek(IN, 0, 0);

	if($pcount == $maxlog){
		$pcount--;
	}

	$no = 1;
	for ($i=0; $i < $pcount; $i++){
		$log[$i] = <IN>;
		if($i == 0){
			($no, $tdate, $tname, $temail, $turl, $tsubject, $tmess, $tpass) = split(/<>/, $log[$i]);
			if($no == ""){
				$no = 1;
			}else{
				$no = int($no);
				$no++;
			}
		}
	}

	$date = &GetDate();
#	my $date;
	unshift(@log, "$no<>$date<>$name<>$email<>$url<>$subject<>$mess<>$pass\n");
	#print $log[0];
	truncate(IN, 0);
	seek(IN, 0, 0);

	$j = @log;
	for($i=0; $i < $j; $i++){
		print IN $log[$i];
	}

	close(IN);

	print "Location: $location?\n\n";
}

sub Delete {
	my($i, $j);
	my @log;

	my($no, $pass);
	my($tno, $tdate, $tname, $temail, $turl, $tsubject, $tmess, $tpass);
	$no = $q->param('no');
	$pass = $q->param('pass');
	
	open(IN,"+< $logfile") || print "Open Error: $logfile";
	flock(IN, 2);
	
	$i=0;
	while(<IN>){
		($tno, $tdate, $tname, $temail, $turl, $tsubject, $tmess, $tpass) = split(/<>/);
		if($no != $tno){
			$log[$i] =  "$tno<>$tdate<>$tname<>$temail<>$turl<>$tsubject<>$tmess<>$tpass";
			$i++;
		}else{
			if(($pass eq $tpass) || ($pass eq &Pass())){
				next;
			}else{
				&PrintError('パスワードが違います');
				close(IN);
				exit(0);
			}
		}
	}
	
	truncate(IN, 0);
	seek(IN, 0, 0);

	$j = @log;
	for($i=0; $i < $j; $i++){
		print IN $log[$i];
	}

	close(IN);
	print "Location: $location?\n\n";
}


exit(0);

