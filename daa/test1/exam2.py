flag = 1
def check(a,low,high):
	if low <= high:
		mid = (low+high)//2
		if a[mid]>mid:
			if a[mid]<=high:
				check(a,a[mid],high)
			check(a,low,mid-1)
		elif a[mid]<mid:
			if a[mid]>=low:
				check(a,low,a[mid])
			check(a,mid+1,high)
		else:
			if a[mid] == mid:
				print(mid)
				global flag
				flag = 0

a=[-10,-8,1,3]
check(a,0,len(a)-1)
if flag:
	print(-1)