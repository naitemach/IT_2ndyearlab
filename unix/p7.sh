#!/bin/bash
echo "Enter marks in unix:"
read u
echo "Enter marks in Java:"
read j
echo "Enter marks in DS:"
read d
average=$(( ($u+$j+$d) / 3 ))
if [ $average -ge 70 ]
then
echo "distinction"
elif [ $average -ge 60 ]
then
echo "First class"
elif [ $average -ge 50 ]
then
echo "Second class"
elif [ $average -ge 40 ]
then
echo "Third class"
else
echo "Fail"
fi

