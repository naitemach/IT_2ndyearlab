sed -i '1i\<html>' a.txt
sed -i '$s/$/\n<html>/g' a.txt
