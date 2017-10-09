echo "Enter java marks"
read j
echo "Enter ds marks"
read d
echo "Enter unix marks"
read u
average=$(( ($j+$d+$u)/3 ))
if [ $average -ge 70 ]
	then
	echo "Distinction"
elif [ $average -ge 60 ]
	then
	echo "First class"
elif [ $average -ge 50 ]
	then
	echo "Second class"
elif [ $average -ge 40 ]
	then
	echo "Third class"
else
	echo "Fail"
fi
