def mergeSort(A,low,high):
	if low < high:
		mid = (low + high)//2
		mergeSort(A,low,mid)
		mergeSort(A,mid+1,high)
		merge(A,low,mid,high)

def merge(A,low,mid,high):
	L=[]
	R=[]
	for i in range(low,mid+1):
		L.append(A[i])
	for i in range(mid+1,high+1):
		R.append(A[i])
	print(A)
	l,r = 0,0
	i=low
	while l<(mid-low+1) and r<(high+mid-2*low+2):
		if L[l] >R[r]:
			A[i]=R[r]
			r += 1
		else:
			A[i] = L[l]
	if l==(mid-low+1):
		while r<(high+mid-2*low+2):
			A[i]=R[r]
			i += 1
			r += 1
	else:
		while l<(mid-low+1):
			A[i]=L[l]
			i += 1
			l += 1



l=[4,6,2,8,3,4,5,1]
print(l)
mergeSort(l,0,7)
print(l)
