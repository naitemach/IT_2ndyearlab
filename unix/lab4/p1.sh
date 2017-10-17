#Write a shell script to list all the files of the current directory 
#having read and write permission to the user
#!/bin/bash
f=`ls -l | cut -c 2-3`
g=`ls`
j=0
for i in $g
do
	a[$j]=$i
	((j=j+1))
done
j=-1
for i in $f
do
	if [ $j -ne -1 ]
    then
	if [ "$i" = "rw" ]
    then
		echo "${a[$j]} has both read and write permission"
	fi
fi
((j=j+1))
done