#!/bin/bash
echo -n "Enter two numbers:"
read a
read b
echo "enter 1 for addition\n2 for subtraction\n3 for mutiplication\n4 for division"
read op
case $op in
	1)
		((sum=a+b))
		echo "the sum is "$sum;;
esac