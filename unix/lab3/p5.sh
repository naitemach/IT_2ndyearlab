#!/bin/bash

for ((i=1;i<=1000;i++))
do
   j=$i
   c=0
   while [ $j -gt 0 ]
   do
     r=`expr $j % 10`
     j=`expr $j / 10`
     rc=`expr $r \* $r \* $r`
     c=`expr $c + $rc`
    done 
    if [ $c -eq $i ]
    then 
    echo $i
    fi   
	
done

