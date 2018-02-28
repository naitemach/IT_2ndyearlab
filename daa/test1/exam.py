

def check(a,low,high):
	if a[low] == low:
		return low
	elif a[low]<low:
		return check(a,low+1,high)
	else:
		if a[low]<=high:
			return check(a,a[low],high)
		else:
			return -1

a=[-3,1,2]
print(check(a,0,len(a)-1))