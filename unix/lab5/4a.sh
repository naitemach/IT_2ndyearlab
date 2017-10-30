#!/bin/bash
a=`ls`
for i in $a
do
	if [ -f $i ]
		then
		echo $i | grep "^[aeiou]"  
	fi
done