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
			if temp.children[index] == i:
				if temp.isEndOfWord:
					return True
				else:
					continue
			else:
				return False

def main():
	t=Trie()
	t.insert("today")
	print(t.search("today"))

if __name__ == '__main__':
	main()

