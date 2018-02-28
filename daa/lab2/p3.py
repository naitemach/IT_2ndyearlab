import time
a = [5,8,2,6,1,4,7,3,10,12,55,74,35,15,400,145,2365,14,0,128,796,426,365]
count = 0
t1 = time.clock()
for i in range(len(a)):
	for j in range(i,len(a)):
		if a[i] > a[j] :
			count += 1
t2 = time.clock()
print("Naive method:")
print(count)
print(t2-t1)


def sortAndCountInv(a,low,high):
	if ( high-low )== 1:
		if a[low] > a[high]:
			temp = a[low]
			a[low] = a[high]
			a[high] = temp
			return 1
		else:
			return 0
	else:
		mid = (low+high)//2
		il = sortAndCountInv(a,low,mid)
		ir = sortAndCountInv(a,mid+1,high)
		isp = sortAndCountSplit(a,low,mid,high)
		return il + ir + isp

def sortAndCountSplit(a,low,mid,high):
	i = 0
	j = 0
	al = a[low:mid+1]
	ar = a[mid+1:high+1]	
	ptr = low

	while i != len(al) and j != len(ar):
		if al[i] > ar[j]:
			a[ptr] = ar[j]
			ptr += 1
			j += 1
		else:
			a[ptr] = al[i]
			ptr += 1
			i += 1
	while j != len(ar):
		a[ptr] = ar[j]
		ptr += 1
		j += 1
	while i != len(al):
		a[ptr] = al[i]
		ptr += 1
		i += 1


	i = 0
	j = 0
	spc = 0
	while j < len(ar):
		while i < len(al):
			if al[i] > ar[j]:
				spc += len(al) - i 
				break
			else:
				i += 1
		j += 1

	return spc

print("Divide and conquer method:")
t1 = time.clock()
print(sortAndCountInv(a,0,21))
t2 = time.clock()
print(t2-t1)
print(a)