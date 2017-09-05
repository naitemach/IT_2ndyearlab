class HashTable(object):
	def __init__(self):
		self.t=[None for i in range(30)]
	def insertKey(self,key,value):
		value=hashvalue(key)
		slot=value%30
		if self.t[slot]==None:
			self.t[slot]=LinkedList()
		self.t[slot].insertAtHead(key,value)
	def searchKey(self,key):
		value=hashvalue(key)
		slot=value%30
		temp=self.t[slot]
		res=temp.searchLinkedList(temp.head,key)
		print(res)
	def keys(self):
		for i in self.t:
			if i!=None:
				if i.head!=None:
					temp=i.head
					while temp!=None:
						print(temp.key,end=",")
						temp=temp.next
		print()

class LinkedList(object):
	def __init__(self):
		self.head=None
	def insertAtHead(self,key,value):
		temp=ListNode()
		temp.key=key
		temp.value=value
		if self.head!=None:
			temp.next=self.head
		self.head=temp
	def searchLinkedList(self,head,key):
		temp=self.head
		if temp==None:
			return false
		else:
			while temp!=None:
				if temp.key==key:
					return True
				temp=temp.next
			return False

class ListNode(object):
	def __init__(self,key=None,value=None):
		self.key=key
		self.value=value
		self.next=None

def hashvalue(key):
	value=0
	for i in key:
		value+=ord(i)
	return value
def main():
	ob=HashTable()
	ob.insertKey("cat",1)
	ob.insertKey("act",2)
	ob.insertKey("cow",3)
	ob.insertKey("parrot",4)
	ob.keys()
	ob.searchKey("cat")

if __name__ == '__main__':
   	main()





















