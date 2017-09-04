#!/bin/sh
area=$(echo "$1*$2"|bc)
echo "Area of the rectangle: $area"