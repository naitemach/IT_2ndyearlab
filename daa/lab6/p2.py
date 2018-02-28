class Edges:
	def __init__ (self,a,b,w):
		self.weight=w
		self.v1=a
		self.v2=b
class Graph:
	def __init__(self):
		self.vertices=[]
		self.edges=[]
		self.D=DisjointSet

	def kruskals(self):
		self.sortEdges()
		T=[]
		for v in self.vertices:
			self.D.makeSet(v)
		for ed in self.edges:
			if self.D.findSet(ed.v1) != self.D.findSet(ed.v2):
				T.append(ed.v1)
				T.append(ed.v2)
				self.D.union(ed.v1,ed.v2)
	def sortEdges(self):
		


