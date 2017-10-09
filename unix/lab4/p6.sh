#!/bin/bash
declare -A a
declare -A b
declare -A c
echo "enter the row of matrix:"
read n
echo "enter the column of matrix:"
read m
echo "Enter the elements of first array:"
for (( i=0; i<n; i++ )); do
	for (( j=0; j<m; j++ )); do
		read a[$i,$j]
	done
done
echo "Enter the elements of second array:"
for (( i=0; i<n; i++ )); do
	for (( j=0; j<m; j++ )); do
		read b[$i,$j]
	done
done
for (( i=0; i<n; i++ )); do
	for (( j = 0; j<m; j++ )); do

		c[$i,$j]=`expr ${a[$i,$j]} + ${a[$i,$j]}`
	done
done
for (( i=0; i<n; i++ )); do
	for (( j=0; j<m; j++ )); do
		echo -n "${c[$i,$j]} "
	done
	echo " "
	
done