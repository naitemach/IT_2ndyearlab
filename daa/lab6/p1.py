class Node:
    def __init__(self,l):
        self.parent = None
        self.rank = 0
        self.value = l

class DisjointSet:
    def __init__(self):
        self.nodes=[]

    def makeSet(self,x):
        x.parent=x
        x.rank=0 
        self.nodes.append(x)

    def findSet(self,x):
        if x.parent != x:
            x.parent = self.findSet(x.parent)
        return x.parent

    def union(self,x,y):
        xroot = self.findSet(x)
        yroot = self.findSet(y)
        if xroot == yroot :
            return
        if xroot.rank  < yroot.rank:
            xroot.parent = yroot
        elif yroot.rank  < xroot.rank:
            yroot.parent = xroot
        else:
            xroot.parent = yroot
            yroot.rank = yroot.rank + 1
    
    def printSet(self):
        foundNode=[]
        ti=1
        for node in self.nodes:
            if node.rank == 0 and node not in foundNode:
                tree=[]
                siblist = self.findSiblings(node)
                for fnode in siblist:
                    foundNode.append(fnode)
                tree.append(siblist)
                while siblist[0].parent.parent != siblist[0].parent:
                    siblist=self.findSiblings(siblist[0])
                    for fnode in siblist:
                        foundNode.append(fnode)
                    tree.append(siblist)
                tree.append([siblist[0].parent])
                print("The tree "+str(ti)+" is:")
                ti= ti+1
                for i in range(len(tree)-1,-1,-1):
                    for j in tree[i]:
                        print(j.value,end=" ")
                    print()

    def findSiblings(self,node):
        tmpn=node.parent
        tmpl=[]
        tmpl.append(node)
        for node2 in self.nodes:
            if node2!=node:
                if node2.parent==tmpn and node2.parent!=node2:
                    tmpl.append(node2)
        return tmpl


D=DisjointSet()
a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')
g=Node('g')
D.makeSet(a)
D.makeSet(b)
D.makeSet(c)
D.makeSet(d)
D.makeSet(e)
D.makeSet(f)
D.makeSet(g)
D.union(a,b)
D.union(c,d)
D.union(c,b)
D.printSet()