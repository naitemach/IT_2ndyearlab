#!/bin/bash
for((i=0;i<=3;i++))
do
echo "Enter the name"
read name
echo $name | cat >> address.lst  
echo "Enter the address"
read address
echo $address | cat >> address.lst
done