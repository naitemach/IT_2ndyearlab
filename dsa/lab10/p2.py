class Node:
	def __init__ (self,l):
		self.label=l
		self.color=None
		self.dist=None
		self.pred=None

class MinHeap(object):
	def __init__(self,n):
		self.array = [Node(i) for i in range(1,n+2)]
		self.size = n
	def getLeft(self,i):
		return self.array[2*i].dist
	def getRight(self,i):
		return self.array[2*i+1].dist

	def heapify(self,i):
		if self.check(i):
			return
		else:
			if 2*i <= self.size:
				max=2*i
				if 2*i+1 <= self.size:
					if self.getRight(i) < self.getLeft(i):
						max=2*i+1
			else:
				if 2*i+1 <= self.size:
					max=2*i+1
				else:
					return
			temp = self.array[max]
			self.array[max] = self.array[i]
			self.array[i] = temp
		if (2*max <= self.size) or (2*max+1 <= self.size):		
			self.heapify(max)
	def check(self,i):
		if 2*i <= self.size:
			if (self.getLeft(i) < self.array[i].dist):
				return False
		if 2*i+1 <= self.size:
			if (self.getRight(i) < self.array[i].dist):
				return False
		return True
	def buildHeap(self):
		for i in range(self.size,0,-1):
			self.heapify(i)
	def extractMin(self):
		if self.size >= 1:
			temp=self.array[1]
			self.array[1]=self.array[self.size]
			self.size -= 1
			self.heapify(1)
			return temp
		else:
			print("empty heap")
	def updatePriority(self,v):
		for j in range(1,self.size+2):
			if self.array[j] == v:
				i=j
				break
		parent= i//2
		if  not self.check(parent):
			temp = self.array[i]
			self.array[i] = self.array[parent]
			self.array[parent] = temp
		if parent//2 > 1:
			self.updatePriority(parent//2)



class Graph:
	def __init__ (self,n,m):
		self.nv=n
		self.ne=m
		self.ew=[[0 for i in range(self.nv)] for i in range(self.nv)]
		self.am=[[0 for i in range(self.nv)] for i in range(self.nv)]
		self.al=[[] for i in range(self.nv)]
		self.vertices=[Node(i) for i in range(self.nv)]
	
	def construct(self):
		print("Enter the edges with edge weight in the format 'start end edge': ")
		for i in range(self.ne):
			s=input()
			s=s.split(' ')
			n1=int(s[0])
			n2=int(s[1])
			self.am[n1][n2] = 1
			self.ew[n1][n2] = int(s[2])

		for i in range(self.nv):
			for j in range(self.nv):
				if self.am[i][j]== 1:
					self.al[i].append(j)
	
	def getAm(self):
		print("The adjacency matrix is:")
		for i in range(self.nv):
			for j in range(self.nv):
				print(self.am[i][j],end=" ")
			print()

	def getAl(self):
		print("The adjacency list is:")
		for i in range(self.nv):
			print("vertex "+str(i)+":",end=" ")
			for j in self.al[i]:
				print(j,end=",")
			print()
	def dijkstra(self,s):
		for i in self.vertices :
			i.dist = 10000000
		s.dist = 0
		h=MinHeap(self.nv)
		temp=1
		for i in self.vertices:
			h.array[temp]=i
			temp += 1
		h.buildHeap()
		while h.size:
			w=h.extractMin()
			for i in self.al[w.label]:
				v=self.vertices[i]
				if w.dist + self.ew[w.label][v.label] < v.dist:
					v.dist = w.dist + self.ew[w.label][v.label]
					h.updatePriority(v)




def main():
	n=int(input("Enter the no of vertices: "))
	m=int(input("Enter the no of edges: "))
	g=Graph(n,m)
	g.construct()
	g.getAl()
	g.getAm()
	si=int(input("Enter the source vertex:"))
	g.dijkstra(g.vertices[si])
	l = 0
	for i in g.vertices:
		print('{:^3}{}{:^4}'.format(l," - ",i.dist))
		l+=1

if __name__ == '__main__':
	main()