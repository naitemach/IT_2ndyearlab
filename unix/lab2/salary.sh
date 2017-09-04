#!/bin/sh
echo -n "Enter basic:"
read basic
dp=$(echo "scale=2;0.5*$basic"|bc)
da=$(echo "scale=2;0.35*($basic+$dp)"|bc)
hra=$(echo "scale=2;0.08*($basic+$dp)"|bc)
ma=$(echo "scale=2;0.03*($basic+$dp)"|bc)
pf=$(echo "scale=2;0.1*($basic+$dp)"|bc)
salary=$(echo "$basic+$dp+$da+$hra+$ma-$pf"|bc)
echo "The salary is:$salary"