class Treenode:
	def __init__(self,key,parent=None,lc=None,rc=None):
		self.parent=parent
		self.key=key
		self.leftchild=lc
		self.rightchild=rc
class Bst:
	def __init__(self,root=None):
		self.root=root
	def insert(self,value):
		n=Treenode(value)
		ptr=self.root
		if ptr == None:
			self.root = n
			return
		while True:
			if value < ptr.key :
				if ptr.leftchild==None :
					break
				ptr=ptr.leftchild
					
			else :
				if ptr.rightchild==None :
					break
				ptr=ptr.rightchild
				
		if value < ptr.key:
			n.parent=ptr
			ptr.leftchild=n
		else :
			n.parent=ptr
			ptr.rightchild=n
	def search(self,value):
		temp=self.root
		if temp == None:
			print("The tree is empty")
		while temp!=None:
			if value == temp.key:
				return True
			elif value < temp.key :
				if temp.leftchild!=None :
					temp=temp.leftchild
				else :
					return False
			else :
				if temp.rightchild!=None :
					temp=temp.rightchild
				else:
					return False
	def minimum(self):
		temp=self.root
		if temp == None:
			print("The tree is empty")
		while temp!=None:
			if temp.leftchild == None:
				return temp.key
			else :
				temp=temp.leftchild
	def maximum(self):
		temp=self.root
		if temp == None:
			print("The tree is empty")
		while temp!=None:
			if temp.rightchild == None:
				return temp.key
			else :
				temp=temp.rightchild
	def traverse(self,n):
		temp=n
		if n.leftchild!=None:
			self.traverse(n.leftchild)	
		print(temp.key,end=" ")
		if n.rightchild!=None:
			self.traverse(n.rightchild)

def main():
	t=Bst()
	t.insert(5)
	t.insert(11)
	t.insert(35)
	t.insert(55)
	t.insert(65)
	t.insert(75)
	t.insert(2)
	t.insert(7)
	t.insert(9)
	print(t.search(9))
	print(t.search(500))
	print(t.minimum())
	print(t.maximum())
	t.traverse(t.root)
if __name__ == '__main__' :
	main()



