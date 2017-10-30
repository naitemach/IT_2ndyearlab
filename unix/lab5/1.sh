#!/bin/bash
echo "Enter the no of entries"
read n
for((i=0;i< n;i++))
do
echo "Enter the name"
read name
echo $name | cat >> address.lst  
echo "Enter the address"
read address
echo $address | cat >> address.lst
done