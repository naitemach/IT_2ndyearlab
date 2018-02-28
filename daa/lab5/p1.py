class Node:
	def __init__ (self,l):
		self.label=l
		self.inEd=0
		self.semNo=0

class Graph:
	def __init__ (self,n,m):
		self.nv=n
		self.ne=m
		self.am=[[0 for i in range(self.nv)] for i in range(self.nv)]
		self.al=[[] for i in range(self.nv)]
		self.vertices=[Node(i) for i in range(self.nv)]
		self.construct()
	
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
	
	def findInEd(self):
		for i in range(self.nv):
			for j in self.al[i]:
				self.vertices[j].inEd += 1
	def findSourceVertices(self):
		self.findInEd()
		s=[]
		for i in range(self.nv):
			if self.vertices[i].inEd == 0:
				s.append(self.vertices[i])

	def findMinSem(self):
		s=self.findSourceVertices()
		k=1
		while(s is not None):
			sn=[]
			for c in s:
				c.semNo=k
				for adv in self.al[c.label]:
					adv.inEd -= 1
					if adv.inEd == 0:
						sn.append(adv)
			s=sn
			k=k+1

