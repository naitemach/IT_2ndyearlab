n=int(input("Enter the no of integers in the array: "))
alist=[]
print("Enter the elements of array")
for i in range(0,n):
	alist.append(int(input("")))
print("list before sorting")
print(alist)
def selectionSort(alist):
   for i in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,i+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[i]
       alist[i] = alist[positionOfMax]
       alist[positionOfMax] = temp
selectionSort(alist)
print(alist)
