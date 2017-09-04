#!/bin/sh
echo -n "Enter the radius:"
read rad
area=$(echo "scale=2;3.14*$rad*$rad"|bc)
echo $area