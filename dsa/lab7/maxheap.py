class MaxHeap(object):
	def __init__(self,n):
		self.array = [None for i in range(1,n+2)]
		self.size = n
	def getLeft(self,i):
		return self.array[2*i]
	def getRight(self,i):
		return self.array[2*i+1]
	def heapify(self,i):
		if self.check(i):
			return
		else:
			if 2*i <= self.size:
				max=2*i
				if 2*i+1 <= self.size:
					if self.getRight(i) > self.getLeft(i):
						max=2*i+1
			else:
				if 2*i+1 <= self.size:
					max=2*i+1
				else:
					return
			temp = self.array[max]
			self.array[max] = self.array[i]
			self.array[i] = temp
			if (2*max <= self.size) or (2*max+1 <= self.size):		
				self.heapify(max)
	def check(self,i):
		if 2*i <= self.size:
			if (self.getLeft(i) > self.array[i]):
				return False
		if 2*i+1 <= self.size:
			if (self.getRight(i) > self.array[i]):
				return False
		return True
	def buildHeap(self):
		for i in range(self.size,0,-1):
			self.heapify(i)
	def extractMax(self):
		if self.size >= 1:
			temp=self.array[1]
			self.array[1]=self.array[self.size]
			self.size -= 1
			self.heapify(1)
			return temp
		else:
			print("empty heap")
	def maximum(self):
		return self.array[1]


h=MaxHeap(5)
h.array[1]=4
h.array[2]=2
h.array[3]=6
h.array[4]=1
h.array[5]=8
print(h.array[0])
h.buildHeap()
for i in range(1,h.size+1):
	print(h.array[i],end=" ")
print(" ")


print("Extracting maximum")
print(h.extractMax())
print("Heap after extracting")
for i in range(1,h.size+1):
	print(h.array[i],end=" ")
print(" ")

print("Extracting maximum")
print(h.extractMax())
print("Heap after extracting")
for i in range(1,h.size+1):
	print(h.array[i],end=" ")
print(" ")

print("Extracting maximum")
print(h.extractMax())
print("Heap after extracting")
for i in range(1,h.size+1):
	print(h.array[i],end=" ")
print(" ")

print("Extracting maximum")
print(h.extractMax())
print("Heap after extracting")
for i in range(1,h.size+1):
	print(h.array[i],end=" ")
print(" ")

print("Extracting maximum")
print(h.extractMax())

