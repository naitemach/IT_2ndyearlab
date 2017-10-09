#!/bin/sh
if [ $1 -le 0 -o $2 -le 0 ]
then
	echo "Invalid commandline inputs\nNumber should be greater the zero"
else
	if [ $1 -gt $2 ]
	then
		res=$(echo "scale=4 ; $2/$1" | bc)
	else
		res=$(echo "scale=4 ; $1/$2" | bc)
		
	fi
	echo $res
    
fi