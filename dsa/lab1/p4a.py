n=int(input("Enter the no of integers in the array: "))
list=[]
print("Enter the elements of array")
for i in range(0,n):
	list.append(int(input("")))
print("list before sorting")
print(list)
for i in range(0,n-1):
	for j in range(0,n-i-1):
		if list[j]>list[j+1]:
			temp=list[j]
			list[j]=list[j+1]
			list[j+1]=temp
print("list after sorting")
print(list)
