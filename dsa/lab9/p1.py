n=int(input("Enter the no of vertices: "))
am=[[0 for i in range(n)] for i in range(n)]
m=int(input("Enter the no of edges: "))
for i in range(m):
	s=input()
	s=s.split(' ')
	n1=int(s[0])
	n2=int(s[1])
	am[n1][n2] = 1
	am[n2][n1] = 1
print("The adjacency matrix is:")
for i in range(n):
	for j in range(n):
		print(am[i][j],end=" ")
	print()
al=[[] for i in range(n)]
for i in range(n):
	for j in range(n):
		if am[i][j]== 1:
			al[i].append(j)
print("The adjacency list is:")
for i in range(n):
	print("vertex "+str(i)+":",end=" ")
	for j in al[i]:
		print(j,end=",")
	print()

