n=int(input("Enter an integer : "))
list=[0,1,1]
for i in range(3,n):
    list.append(list[i-1]+list[i-2])
print("The first n fibonacci series is")
print(list)