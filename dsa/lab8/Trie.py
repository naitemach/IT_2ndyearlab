class TrieNode:
    def __init__(self):
        self.children=[None for i in range(26)]
        
class Trie:
    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return TrieNode()

    def insert(self,key):
        d=list(key)
        temp=self.root
        for i in range(len(d)):
            index=ord(d[i])-ord('a')
            if temp.children[index] is None :
                temp.children[index]=d[i]
                temp.children[index]=self.getNode()
                temp=temp.children[index]
            else:
                temp=temp.children[index]

    def search(self,key):
        d=list(key)
        temp=self.root
        for i in range(len(d)):
            index=ord(d[i])-ord('a')
            if temp.children[index]==None:
                return False
            elif temp.children[index]!=None and i!=(len(d))-1:
                temp=temp.children[index]
            else:
                temp=temp.children[index]
                return True
                

t=Trie()
t.insert("apple")
t.insert("mango")
t.insert("papaya")
t.insert("strawberry")
t.insert("peach")
t.insert("action")
print(t.search("apple"))
print(t.search("bannana"))
print(t.search("goat"))
print(t.search("peach"))
print(t.search("action"))

            
