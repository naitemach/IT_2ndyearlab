#!/bin/bash
echo -n "Enter n:"
read n
for((i=0;i<n;i++))
do
	read temp
	((sum=sum+temp))
done
average=$(echo "scale=2;$sum/$n"|bc)
echo "Average:$average"