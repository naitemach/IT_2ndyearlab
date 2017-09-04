#!/bin/sh
if [ $# -eq 0 ] ; then
echo "Error-Number missing from the command line argument"
echo "syntax : $0 number"
echo "use to print multiplication table for given number"
fi
n=$1
i=1
while [ $i -le 10 ]
do
echo "$n*$i=`expr $i \* $n`"
i=`expr $i + 1`
done