class TrieNode(object):
	def __init__(self):
		self.children=[None]*26
		self.isEndOfWord=False
		self.count=0
		self.list=[]
class Trie(object):
	def __init__(self):
		self.root = TrieNode()
		self.count = 0
	def charToIndex(self,c):
		return ord(c)-ord('a')
	def insert(self,key):
		temp = self.root
		for i in key:
			index = self.charToIndex(i)
			if not temp.children[index]:
				temp.children[index] = TrieNode()
			temp = temp.children[index]
		temp.isEndOfWord = True
		temp.count =  temp.count + 1
		self.count = self.count + 1
		temp.list.append(self.count)

	def search(self,key):
		temp = self.root
		for i in key:
			index = self.charToIndex(i)
			if not temp.children[index]:
				return False
			temp = temp.children[index]
		if temp != None and temp.isEndOfWord :
			print("the word has occured",temp.count)
			print(temp.list)
			return True

t=Trie()
file=open('Text.txt','r')
content=list(file)
file.close()
content=[x.strip() for x in content]
content=[x.strip(',.') for x in content]
content=''.join(content)
content=content.lower()
content=content.split(".")
content=''.join(content)
content=content.split(",")
content=''.join(content)
content=content.split(" ")
print(content)
for i in range(len(content)):
	y="".join(content[i])
	t.insert(y)
print(t.search("between"))
print(t.search("other"))
print(t.search("the"))
print(t.search("devices"))