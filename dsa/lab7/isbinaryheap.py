class BinaryTree:
	def  __init__(self):
		self.root=None
class TreeNode:
	def __init__(self,val):
		self.val=val
		self.left=None
		self.right=None
		self.parent=None

def isBinaryHeap(b):
	temp = b
	if temp.left != None:
		if temp.val < temp.left.val:
			return False
		if temp.right != None:
			if temp.val < temp.right.val:
				return False
		else:
			if temp.left.left:
				return False
	else:
		if temp.right != None:
			return False
	if temp.left != None:		
		if isBinaryHeap(temp.left):
			return False
	if temp.right != None:
		if isBinaryHeap(temp.right):
			return False
	return True

def main():
	b = BinaryTree()
	temp=TreeNode(6)
	b.root=temp
	temp2=TreeNode(4)
	temp.left = temp2
	temp2.parent = temp
	temp3=TreeNode(3)
	temp.right= temp3
	temp3.parent = temp
	temp4=TreeNode(2)
	temp2.left= temp4
	temp4.parent=temp2
	temp5=TreeNode(1)
	temp2.right= temp5
	temp5.parent=temp2
	flag=0
	print(isBinaryHeap(b.root))

if __name__ == '__main__':
	main()