class TreeNode:
	def __init__(self,k=None):
		self.key=k
		self.parent=None
		self.left=None
		self.right=None
	def minimum(self):
		temp = self
		while temp.left != None:
			temp=temp.left
		return temp

	def maximum(self):
		temp = self
		while temp.right != None:
			temp=temp.right
		return temp

	def predecessor(self):
		if self.left != None:
			return self.left.maximum()
		else:
			y = self.parent
			n = self
			while y.right != n and y != None:
				n=y
				y = y.parent
			return y

	def successor(self):
		if self.right != None:
			return self.right.minimum()
		else:
			n = self
			y = self.parent
			while y.left != n and y != None:
				n = y
				y = y.parent
			return y

	def getHeight(self):
		if isLeaf(self):
			return 1
		else:
			lefth = getHeight(self.left)
			righth = getHeight(self.right)
			if lefth+1 >= right+1:
				return lefth+1
			else:
				return righth+1

class AvlTree:
	def __init__(self)
		self.root=TreeNode()

	def search(self,key):
		temp = self.root
		while temp != None:
			if key > temp.key:
				temp = temp.right
			elif key < temp.key:
				temp = temp.left
			elif key = temp.key:
				return True
		return False

	def isBalanced(self,n):
		
		if abs(getheight(n.left) - getHeight(n.left)) >= 2:
			return False
		self.isbalanced(n.left)
		self.isbalanced(n.right)
		return True 


	def insert(self,key):
		temp = self.root
		temp2 = TreeNode()
		temp2.value = key
		if temp == None:
			temp.key = key
			return
		while True:
			if key > temp.key:
				if temp.right == None:
					temp.right=temp2
					return
				else:
					temp = temp.right
			else:
				if temp.left == None:
					temp.left=temp2
					return
				else:
					temp = temp.left
		temp2 = TreeNode()
		temp2.value = key
