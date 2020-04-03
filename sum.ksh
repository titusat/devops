#!/bin/bash
# Calculate the sum of two integers with pre initialize values
 
a=152
b=3000
 
sum=$(( $a + $b ))
 
echo $sum >> Sum.txt
