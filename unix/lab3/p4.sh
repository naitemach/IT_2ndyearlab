#!/bin/bash
for i in 0 1 2 3 4 5 6 7 8 9
do
	q=`expr $i + 1`
	echo Enter no $q
	read no[$i]
done
pos=0
neg=0
zero=0
for i in 0 1 2 3 4 5 6 7 8 9 
do
	if [ ${no[$i]} -lt 0 ] ; then
        neg=`expr $neg + 1`
    elif [ ${no[$i]} -eq 0 ] ; then
    	zero=`expr $zero + 1`
    else
    	pos=`expr $pos + 1`
    fi
done
echo "no of negetive numbers is $neg"
echo "no of positive numbers is $pos"
echo "no of zeros is $zero"
echo "numbers in acending order:"
for ((i=0;i<9;i++))
do
	for ((j=0;j<9-$i;j++))
	do
		k=`expr $j + 1`
		if [ ${no[$j]} -gt ${no[$k]} ]
	    then
	        temp=${no[$j]}
	        no[$j]=${no[$k]}
	        no[$k]=$temp
	    fi
	done
done
for i in 0 1 2 3 4 5 6 7 8 9 
do
	
	echo -n "${no[$i]}"
	echo -n " "
done
echo ""


