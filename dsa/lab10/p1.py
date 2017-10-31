class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

class Node:
	def __init__ (self,l):
		self.label=l
		self.color=None
		self.dist=None
		self.pred=None
		self.start=None
		self.end=None

class Graph:
	def __init__ (self,n,m):
		self.nv=n
		self.ne=m
		self.am=[[0 for i in range(self.nv)] for i in range(self.nv)]
		self.al=[[] for i in range(self.nv)]
		self.vertices=[Node(i) for i in range(self.nv)]
		self.time=None

	def construct(self):
		print("Enter the edges: ")
		for i in range(self.ne):
			s=input()
			s=s.split(' ')
			n1=int(s[0])
			n2=int(s[1])
			self.am[n1][n2] = 1
			self.am[n2][n1] = 1
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
	
	def BFS(self,s):
		for i in range(self.nv):
			if i != s.label:
				self.vertices[i].dist=None
				self.vertices[i].color="white"
				self.vertices[i].pred=None
		s.dist=0
		s.color="grey"
		q=Queue()
		print("visited the vertex "+ str(s.label))
		print("Distance from the source vertex is "+str(s.dist))
		q.enqueue(s)
		while not q.isEmpty():
			u=q.dequeue()
			for i in self.al[u.label]:
				v=self.vertices[i]
				if v.color=="white":
					v.dist=u.dist + 1
					v.color="grey"
					v.pred=u
					print("visited the vertex "+ str(v.label))
					print("Distance from the source vertex is "+str(v.dist))
					q.enqueue(v)
				u.color="black"

	def DFS(self,u):
		self.time += 1
		u.start = self.time
		u.color = 'grey'
		for i in self.al[u.label]:
			if self.vertices[i].color=="white":
				self.DFS(self.vertices[i])
				self.vertices[i].pred=u
		u.color="black"
		self.time += 1
		u.end = self.time 
		print("The vertex "+str(u.label)+" start time: "+str(u.start)+" end time: "+str(u.end))


def main():
	n=int(input("Enter the no of vertices: "))
	m=int(input("Enter the no of edges: "))
	g=Graph(n,m)
	g.construct()
	g.time = 0
	for i in g.vertices:
		i.color='white'
	g.DFS(g.vertices[0])

if __name__ == '__main__':
	main()