osch=0
echo "1.unix(sun os)"
echo "2.linux(red hat)"
echo -n "select your os choice[1 or 2]?"
read osch
if [ $osch -eq 1 ] ; then
echo "you pick up unix(sun os)"
else if [ $osch -eq 2 ] ; then
echo "you pick up linux(Red hat)"
else 
echo "you dont like unix/linux os"
fi
fi