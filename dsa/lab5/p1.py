class TreeNode:
	def __init__(self,value):
		self.val=value
		self.parent=None
		self.right=None
		self.left=None

class BinSearchTree:
	def __init__(self,rootval):
		self.root=TreeNode(rootval)


	def search(self,key):
		trav=self.root
		
		while trav!=None:
			if trav.val==key:
				return trav
			if trav.val>key:
				trav=trav.left
			else:
				trav=trav.right
		else:
			return


	def insert(self,val):
		node=TreeNode(val)
		temp=self.root
		if temp.val>=val:
			prev=temp
			temp=temp.left
			flag=0
		else:
			prev=temp
			temp=temp.right
			flag=1
		node.parent=prev
		if flag==0:
			prev.left=node
		else:
			prev.right=node

	def delete(self,val):
		node=self.search(val)
		if node.left==None and node.right==None:
			if node.parent.val<node.val:
				node.parent.right=None
			else:
				node.parent.left=None
			node.parent=None
		elif node.left==None or node.right==None:
			if node.left==None:
				curr=node.right
				node.right=None
			else:
				curr=node.left
				node.left=None
			curr.parent=node.parent
			if node.parent.val<node.val:
				node.parent.right=curr
			else:
				node.parent.left=curr
			node.parent=None
		else:
			curr=self.successor()
			curr.parent=node.parent
			curr.left=node.left
			curr.right=node.right
			node.parent=None
			node.left=None
			node.right=None



	def minimum(self):
		temp=self.root
		while temp.left!=None:
			temp=temp.left
		return temp


	def maximum(self):
		temp=self.root
		while temp.right!=None:
			temp=temp.right
		return temp

	def predecessor(self):
		temp=self.root.left
		while temp.right!=None:
			temp=temp.right
		return temp

	def successor(self):
		temp=self.root.right
		while temp.left!=None:
			temp=temp.left
		return temp


def preorderTree(trav):
	if trav:
		print(trav.val),
	
	if trav.left!=None:
		preorderTree(trav.left)
	if trav.right!=None:
		preorderTree(trav.right)



def main():
	node=BinSearchTree(25)
	node.insert(12)
	node.insert(15)
	s=node.search(30)
	node.insert(123)
	node.insert(45)
	print(s)
	print(node.minimum().val)
	print(node.maximum().val)
	print()
	print(node.predecessor().val)
	print()
	print(node.successor().val)
	print() 	
	preorderTree(node.root)
	node.delete(12)
	print() 	
	preorderTree(node.root)
	print(node.search(12))

if __name__ == '__main__':
	main()