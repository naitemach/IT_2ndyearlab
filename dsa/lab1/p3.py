n=int(input("Enter an integer: "))
for i in range(2,n):
	if n%i==0:
		print("False")
		break
else:
	print("True")