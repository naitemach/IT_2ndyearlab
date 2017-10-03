import operator

class TreeNode:
	def __init__(self,value):
		self.val=value
		self.parent=None
		self.right=None
		self.left=None

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getRootVal(self):
		return self.val


class Parsetree:
	def __init__(self):
		self.root=TreeNode('')

	def insert(self,exp):
		tree=self.root
		curr=tree
		for i in exp:
			if i == '(':
				temp=TreeNode('')
				curr.left=temp
				temp.parent=curr
				curr=temp
			if i in ['+', '-', '*', '/']:
				curr.val=i
				temp=TreeNode('')
				curr.right=temp
				temp.parent=curr
				curr=temp

			if i==')':
				curr=curr.parent

			if i.isdigit():
				curr.val=i
				curr=curr.parent


def printPrefix(trav):
	if trav:
		print(trav.val,end=" ")
	
	if trav.left!=None:
		printPrefix(trav.left)
	if trav.right!=None:
		printPrefix(trav.right)

def printInOrder(trav):
	if trav.left!=None:
		printInOrder(trav.left)
	print(trav.val,end=" ")
	if trav.right!=None:
		printInOrder(trav.right)

def printPostFix(trav):
	if trav:
		printPostFix(trav.left)

		printPostFix(trav.right)

		print(trav.val,end=" ")

def postordereval(tree): 
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv} 
	res1 = None 
	res2 = None 
	if tree: 
		res1 = postordereval(tree.getLeft()) 
		res2 = postordereval(tree.getRight()) 
		if res1 and res2: 
			return opers[tree.getRootVal()](int(res1),int(res2))
		else: 
			return tree.getRootVal()

def main():
	pt=Parsetree()
	pt.insert('((2*3)+(6/3)')
	printPrefix(pt.root)
	print()
	printPostFix(pt.root)
	print()
	printInOrder(pt.root)
	print()
	print(postordereval(pt.root))
    
if __name__ == '__main__':
	main()
