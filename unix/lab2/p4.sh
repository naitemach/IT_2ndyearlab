echo "Enter the password"
stty -echo
read password
stty echo
echo "Your password is $password"