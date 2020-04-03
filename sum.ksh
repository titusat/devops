#!/bin/bash
# Calculate the sum of two integers with pre initialize values
# in a shell script
 
a=10
b=300
 
sum=$(( $a + $b ))
 
echo $sum >> Sum.txt
