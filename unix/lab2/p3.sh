select k in date cal who whoiam tty quit
do
case $k in
	date ) date;;
	cal ) cal;;
    who ) who;;
    whoiam ) who i am ;;
    tty ) tty;;
	quit ) echo "bye bye"
	       exit;;
	 *) echo "Try again" 	
esac
done