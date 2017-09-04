#!/bin/sh
echo -n "simple interest:"
echo "scale=2;$1*$2*$3/100"|bc
