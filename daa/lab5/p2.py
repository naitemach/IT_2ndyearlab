def findMajority(A,start,end):
	mid=(start+end)//2
	if mid == start:
		if A[start]==A[end]:
			return A[mid]
		return None
	else:
		x=findMajority(A,start,mid)
		y=findMajority(A,mid,end)
		if findCount(x,A,start,end) > (end-start+1)/2:
			return x
		elif findCount(y,A,start,end) > (end-start+1)/2:
			return y
		else:
			return None

def findCount(y,A,start,end):
	count =0
	for i in A[start:end+1]:
		if i == y:
			count += 1

	return count

A=[1,1,1,1,1,1,2,2,2,2,2]
print(findMajority(A,0,10))

