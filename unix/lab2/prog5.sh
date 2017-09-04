#!/bin/sh
echo -n "Enter two numbers:"
read na
read nb 
echo -n "Enter the operator:"
read op
result=$(echo "$na$op$nb"|bc)
echo $result