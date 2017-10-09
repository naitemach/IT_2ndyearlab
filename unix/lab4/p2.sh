#Write a shell script to checks if name given is file or directory
#and if it is file then it should display content and if it is a directory then it should display the list
#!/bin/sh
echo "Enter a file/directory name"
read name
if [ -f $name ]
	then
	cat $name
fi
if [ -d $name ]
	then
	cd $name
	ls
fi
