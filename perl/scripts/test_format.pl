#!/usr/bin/env perl
use strict;
use warnings;

sub test_func {
    my ($param) = shift;
    print "Hello $param\n";
}

test_func("World");
