#!/bin/sh
if [ $1 -le 0 -o $2 -le 0 ]
then
	echo "Invalid commandline inputs\nNumber should be greater the zero"
else
	if[ $1 -gt $2 ];then
		((res=$2/$1))
	else
		((res=$1/$2))
	fi
    echo res
fi