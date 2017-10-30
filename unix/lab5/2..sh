#!/bin/bash
t=`date +%H`
if [ $t -ge 0 -a $t -lt 12 ]
	then
	echo "Good Moring"
elif [ $t -ge 12 -a $t -lt 18 ]
	then
	echo "Good Afternoon"	
elif [ $t -ge 18 -a $t -lt 20 ]
	then
	echo "Good Evening"
else
	echo "Good Night"
fi