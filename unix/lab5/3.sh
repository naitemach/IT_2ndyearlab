select k in Add Delete Find Exit
do
	case $k in
		Add )
			echo "Enter rollno"
			read r
			echo $r | cat >> database.txt
			echo "Enter semester"
			read s
			echo $s | cat >> database.txt
			echo "Enter name"
			read n
			echo $n | cat >> database.txt
			echo "Enter marks in dsa"
			read m1
			echo $m1 | cat >> database.txt
			echo "Enter marks in java"
			read m2
			echo $m2 | cat >> database.txt
			echo "Enter marks in unix"
			read m3
			echo $m3 | cat >> database.txt
			;;
		Delete )
			echo "Enter the rollno"
			read r
			l=`grep -n -i $r database.txt | cut -f1 -d:`
			for((i=1;i<=6;i++))
			do
			sed -i "${l}d" database.txt
			done
			;;
		Find )
			echo "Enter the rollno"
			read r
			res=`grep -i $r database.txt`
			if [ $? == 0 ]
				then 
				echo "Record Found"
			else
				echo "Record Not Found"
			fi
			l=`grep -n -i $r database.txt | cut -f1 -d:`
			e=`expr $l + 5`
			for((i=l;i<=e;i++))
			do
			sed -n "${i}p" database.txt
			done
			;;
		Exit)
			exit
			;;

	esac
done