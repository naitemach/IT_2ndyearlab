#!/bin/sh

echo "The current home directory is $HOME"
USER=`whoami`
echo "User name: $USER"
dt=`date +%m/%d/%y`
echo "Todays date : $dt"
nouser=`who | wc -l`
echo "No of users are : $nouser"
terminal=`tty `
no=`basename $terminal`
echo "The terminal no is : $no"
