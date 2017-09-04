if [ -z $1 ]
then
rental="***unknown vehicle***"
elif [ -n $1 ]; then
	rental=$1
fi
case $rental in
"car") echo " For $rental Rs.20 per k/m";;
"van") echo " For $rental Rs.10 per k/m";;
"jeep") echo "For $rental Rs.5 per k/m";;
"bicycle") echo "For $rental 20 paise per k/m";;
*) echo "sorry,I can not get a $rental for you";;    
esac