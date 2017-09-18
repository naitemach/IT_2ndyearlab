#!/bin/bash
ls | cat > a.txt
a=`cat a.txt`
f=0
d=0
for i in $a
do 
echo $i
if [ -f $i ]
	then
	echo "It is a file"
	f=`expr $f + 1`
elif [ -d $i ]
	then
	echo "It is a directory"
	d=`expr $d + 1`
fi
done
echo "There are $f files"
echo "There are $d directory"
