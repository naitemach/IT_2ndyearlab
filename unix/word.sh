#!/bin/bash
echo "enter an string"
read s
len=$(echo $s | wc -c)
((len=len-1))
for (( i=1;i<=$len; i++))
do
	a[$i]=$(echo $s | cut -c $i)
done
flag=0
j=$len
((len=len/2))
for (( i=1;i<=$len;i++ ))
do
	if [ ${a[$i]} == ${a[$j]} ]; then
		((j=j-1))
	else
        flag=1
	fi
done
if [ $flag -eq 0 ]; then
	echo "Its a palindrome"
else
	echo "Its not a palindrome"
fi