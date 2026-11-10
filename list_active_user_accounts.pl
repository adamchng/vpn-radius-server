#!/usr/bin/perl

my @users;
my $filename = '/etc/shadow';

open(FH, '<', $filename) or die $!;

while(<FH>) {
        my $string_len = length($_);
        # filter only actual user accounts with passwords
        if($string_len > 80) {
                #print $_ . ' ' . $string_len . "\n";
                if(/^\S+\:\!/) {
                        # users who have their accounts locked out
                        #print $_ . ' ' . $string_len . "\n";
                } elsif (/^root/) {
                        # filter out root account
                } else {
                        # active users
                        $_ =~ s/^([^:]+)\:(.*)/$1/g;
                        push(@users, $_);
                }
        }
}

print "\n";
print "-----------------------------------------------\n";
system("date");
print "vpn.xxx.com List of Active User Accounts\n";
print "-----------------------------------------------\n";
my @sortedusers = sort @users;
foreach(@sortedusers) {
        print $_;
}
print "---------------------END-----------------------\n\n";

close(FH);
