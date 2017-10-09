#!/bin/bash
declare -A a
declare -A b
declare -A c
echo "enter the number of elemnts:"
read n
echo "Enter the elements of first array:"
for (( i=0; i<n; i++ )); do
	for (( j=0; j<n; j++ )); do
		read a[$i,$j]
	done
done
echo "Enter the elements of second array:"
for (( i=0; i<n; i++ )); do
	for (( j=0; j<n; j++ )); do
		read b[$i,$j]
	done
done
for (( i=0; i<n; i++ )); do
	for (( j = 0; j<n; j++ )); do

		c[$i,$j]=`expr ${a[$i,$j]} + ${a[$i,$j]}`
	done
done
for (( i=0; i<n; i++ )); do
	for (( j=0; j<n; j++ )); do
		echo -n "${c[$i,$j]} "
	done
	echo " "
	
done