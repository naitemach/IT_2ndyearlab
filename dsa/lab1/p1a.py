n=int(input("Enter an integer: "))
factorial=1
for i in range(n,0,-1):
    factorial*=i
print(factorial)