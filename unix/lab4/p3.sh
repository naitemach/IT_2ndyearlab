#!/bin/sh
echo "Enter file 1 name"
read name1
echo "Enter file 2 name"
read name2

if [ -f $name1 ]
	then
if [ -f $name2 ]
	then
	cat $name2 | cat >> $name1
	echo "After appending"
	cat $name1
else
    echo "File 2 doesnt exits"
fi
else
	echo "File 1 doesnt exits"
fi
