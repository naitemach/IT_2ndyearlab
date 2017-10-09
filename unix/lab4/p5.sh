#!/bin/bash
echo "Enter File name"
read f
p=`ls -l $f`
echo "Displaing rights in the format read-write-execute"
echo "Owner rights : ${p:1:3}"
echo "Group rights : ${p:4:3}"
echo "User rights : ${p:7:3}"
