class Node:
	def __init__(self,x=None,y=None,z=None,p=None):
		self.key=x
		self.lc=y
		self.rc=z
		self.p=p
		self.h=1

class Avl:

	def __init__(self):
		self.head=Node()

	def ht(self,p):
		if p.lc==None and p.rc==None:
			return 1
		elif p.lc==None and p.rc!=None:
			return p.rc.h + 1
		elif p.rc==None and p.lc!=None:
			return p.lc.h + 1
		else:
			l=p.lc.h
			r=p.rc.h
		if l>r:
			return l+1
		else:
			return r+1

	def bal(self,p):
		if p.lc==None and p.rc==None:
			return None
		elif p.lc==None and p.rc!=None:
			if p.h>2:
				return p
			else:
				return None
		elif p.rc==None and p.lc!=None:
			if p.h>2:
				return p
			else:
				return None
		else:
			l=p.lc.h
			r=p.rc.h
		if l-r>1 or l-r<-1:
			return p
		else:
			return None

	def rotr(self,z):
		y=z.lc
		tmp=y.rc
		y.rc=z
		y.p=z.p
		z.lc=tmp
		if z.p==self.head:
			self.head.lc=y
		else:
			if z.p.key>z.key:
				z.p.lc=y
			else:
				z.p.rc=y
		z.p=y
		if tmp!=None:
			tmp.p=z
		while z!=self.head:
			z.h=self.ht(z)
			z=z.p

	def rotl(self,z):
		y=z.rc
		tmp=y.lc
		y.lc=z
		y.p=z.p
		z.rc=tmp
		if z.p==self.head:
			self.head.lc=y
		else:
			if z.key<z.p.key:
				z.p.lc=y
			else:
				z.p.rc=y
		z.p=y
		if tmp!=None:
			tmp.p=z
		while z!=self.head:
			z.h=self.ht(z)
			z=z.p

	def search(self,root,x):
		if root==None:
			print(x,"NOT FOUND")
			return None
		else:
			if x>root.key:
				return self.search(root.rc,x)
			elif x<root.key:
				return self.search(root.lc,x)
			else:
				return root
	
	def prede(self,root,x):
			z=self.search(root,x)
			if z== None or z==self.min(root):
				print("No Predecessor")
				return
			if z.lc!=None:
				return(self.max(z.lc))
			else:
				z=z.p
				while(z.key>x):
					z=z.p
				return z

	def suce(self,root,x):
		z=self.search(root,x)
		if z==None or z==self.max(root):
			print("No Successor ")
			return 
		if z.rc!=None:
			return(self.min(z.rc))
		else:
			z=z.p
			while z.key<x:
				z=z.p
			return z

	def min(self,root):
		while(root.lc!=None):
			root=root.lc
		return root

	def max(self,root):
		while(root.rc!=None):
			root=root.rc
		return root

	def insert(self,root,new):
		if root==None:
			self.head.lc=Node(new,None,None,self.head)
			return
		while root != None:
			paa=root
			if (root.key>new):
				root=root.lc
			else:
				root=root.rc
		tmp=Node(new,None,None,paa)
		if paa.key>new:
			paa.lc=tmp
		else:
			paa.rc=tmp
		z=None
		while(tmp.p.key!=None):
			tmp.p.h=self.ht(tmp.p)
			if z==None:
				z=self.bal(tmp.p)
			tmp=tmp.p

		if z!=None:
			if new<z.key:
				y=z.lc
				if new<y.key:
					self.rotr(z)
				else:
					self.rotl(y)
					self.rotr(z)
			else:
				y=z.rc
				if new>y.key:
					self.rotl(z)
				else:
					self.rotr(y)
					self.rotl(z)

	def preord(self,root):
		
		if(root==None):
			return
		else:
			print("key=",root.key,"height =",root.h)

			self.preord(root.lc)
			self.preord(root.rc)

	def recurse(self,root,tmp):
		z=None
		while tmp!=self.head:
			tmp.h=self.ht(tmp)
			if z==None:
				z=self.bal(tmp)
			tmp=tmp.p
		if z!=None:
			if x<z.key:
				y=z.rc
				left,right=0,0
				if y.lc !=None:
					left=y.lc.h
				if y.rc !=None:
					right=y.rc.h
				if left > right:
					x=y.lc
					self.rotr(y)
					self.rotl(z)
					self.recurse(self.head.lc,x)

				else:
					x=y.rc
					self.rotl(z)
					self.recurse(self.head.lc,x)
			else:
				y=z.lc
				left,right=0,0
				if y.lc !=None:
					left=y.lc.h
				if y.rc !=None:
					right=y.rc.h
				if left > right:
					x=y.lc
					self.rotr(z)
					self.recurse(self.head.lc,x)
				else:
					x=y.rc
					self.rotl(y)
					self.rotr(z)
					self.recurse(self.head.lc,x)
	def delete(self,root,x):
		old=self.search(root,x)
		if old==None:
			return
		if old.lc==None and old.rc==None:
			tmp=old.p
			if tmp.lc==old:
				tmp.lc=None
			else:
				tmp.rc=None
			old.p=None
			self.recurse(self.head.lc,tmp)				
		elif old.lc==None and old.rc!=None:
			old.key=old.rc.key
			self.delete(old.rc,old.rc.key)

		elif old.lc!=None and old.rc==None:
			old.key=old.lc.key
			self.delete(old.lc,old.lc.key)

		else:
			new=self.min(old.rc)
			old.key=new.key
			self.delete(old.rc,new.key)

t=Avl()
t.insert(t.head.lc,15)
t.insert(t.head.lc,5)
t.insert(t.head.lc,16)
t.insert(t.head.lc,1)
t.insert(t.head.lc,20)
t.insert(t.head.lc,7)
t.insert(t.head.lc,18)
t.insert(t.head.lc,12)
print("Preorder traversal:")
t.preord(t.head.lc)
t.delete(t.head.lc,16)
print("Preorder traversal:")
t.preord(t.head.lc)
print()
