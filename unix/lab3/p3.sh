#!/bin/bash
for i in 1 2 3 4 5
do
	echo Enter no $i
	read no[$i]
done

minc=1
maxc=1
for i in 1 2 3 4 5
do
	if [ $i -eq 1 ]
    then
        max=${no[$i]}
        min=${no[$i]}
    else
    if [ ${no[$i]} -lt $min ]
    then
        min=${no[$i]}
        minc=1
    elif [ ${no[$i]} -eq $min ]
    then 
        minc=`expr $minc + 1`
    fi 
    if [ ${no[$i]} -gt $max ]
    then
        max=${no[$i]}
        maxc=1
    elif [ ${no[$i]} -eq $max ]
    then 
        maxc=`expr $maxc + 1`
    fi
    fi
done
echo "The min no is $min"
echo "There are $minc numbers with minimum value"
echo "The max no is $max"
echo "There are $maxc numbers with maximum value"

