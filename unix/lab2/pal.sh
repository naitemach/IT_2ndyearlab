echo -n "Enter number : "
read n
sd=0

on=$n
while [ $n -gt 0 ]
do
    sd=$(( $n % 10 )) 
    n=$(( $n / 10 ))
    rev=$(($rev * 10 + $sd))
    rev=$( echo ${rev}${sd})
done
 
if [ $on -eq $rev ];
then
  echo "Number is palindrome"
else
  echo "Number is NOT palindrome"
fi