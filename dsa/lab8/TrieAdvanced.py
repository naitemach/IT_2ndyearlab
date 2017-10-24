class TrieNode:
    def __init__(self):
        self.children=[None for i in range(26)]
        self.end=False
        self.count=0
        self.list=[]
        
        

class Trie:
    def __init__(self):
        self.root=self.getNode()
        self.count=0

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
        temp.end=True
        temp.count=temp.count+1
        self.count=self.count+1
        temp.list.append(self.count)
        
        

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
for i in range(len(content)):
    y="".join(content[i])
    t.insert(y)

print(t.search("between"))
print(t.search("other"))
print(t.search("the"))
print(t.search("devices"))

            
