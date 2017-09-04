#!/bin/sh
if [ $# -eq 0 ] ; then
echo "Error-Number missing from the command line argument"
echo "syntax : $0 number"
echo "use to print multiplication table for given number"
fi
n=$1
for i in 1 2 3 4 5 6 7 8 9 10
do
echo "$n*$i=`expr $i \* $n`"
done