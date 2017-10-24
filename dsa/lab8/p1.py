class TrieNode(object):
	def __init__(self):
		self.children=[None]*26
		self.isEndOfWord=False
class Trie(object):
	def __init__(self):
		self.root = TrieNode()
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
	def search(self,key):
		temp = self.root
		for i in key:
			index = self.charToIndex(i)
			if not temp.children[index]:
				return False
			temp = temp.children[index]
		return temp != None and temp.isEndOfWord

def main():
	t=Trie()
	keys = ["the","a","there","answer","any","by","their"]
	output = ["Not present in trie","Present in tire"]
	for key in keys:
		t.insert(key)
	print("{}-{}".format("the",output[t.search("the")]))
	print("{}-{}".format("these",output[t.search("these")]))
	print("{}-{}".format("their",output[t.search("their")]))
	print("{}-{}".format("ans",output[t.search("ans")]))

if __name__ == '__main__':
	main()

