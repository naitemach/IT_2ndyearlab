class TreeNode:

    def __init__(self,k=None):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

class BST:

    def __init__(self,r=None):
        self.root = r

    def insert(self,x):
        n = TreeNode()
        n.key = x
        temp = self.root
        if temp == None:
            self.root = n
            return

        while True:
            if temp.key < x:
                if temp.right == None:
                    break
                temp = temp.right
            elif temp.key > x:
                if temp.left == None:
                    break
                temp = temp.left
        if temp.key < x:
            temp.right = n
            n.parent = temp
        else:
            temp.left = n
            n.parent = temp

    def search(self,k):
        temp = self.root
        while temp != None:
            if temp.key == k:
                return True
            elif k > temp.key:
                temp = temp.right
            else:
                temp = temp.left
        return False
    def minimum(self,n):
        temp = n
        if temp == None:
            return temp
        while temp.left != None:
            temp = temp.left
        return temp
       

    def maximum(self,n):
        temp = n
        while temp != None:
            if temp.right != None:
                temp = temp.right
                continue
            return temp
        return None

    def successor(self,n):
        if n.right != None:
            return self.minimum(n.right)
        y = n.parent
        while y.left != n and y != None:
            n = y
            y = n.parent
        return y

    def predecessor(self,n):
        if n.left != None:
            return self.maximum(n.left)
        y = n.parent
        while y.right != n and y != None:
            n = y
            y = n.parent
        return y

    def isLeaf(self,n):
        if n.left == None and n.right == None:
            return True
        return False

    def delete(self,n):
        if n.left != None and n.right != None:
            y = self.predecessor(n)
            p = y.parent
            n.key = y.key
            self.delete(y)
        elif self.isLeaf(n):
            if n.parent ==None:
                self.root=None
                return
            p = n.parent
            if p.right == n:
                p.right = None
            else:
                p.left = None
        else:
            p = n.parent
            if p==None:
                if n.right != None:
                   self.root = n.right
                   n.right.parent=None
                else:
                   self.root = n.left
                   n.left.parent=None
                return
            if n.right != None:
                c = n.right
            else:
                c = n.left
            if p.right == n:
                p.right = c
            else:
                p.left = c
        if n.parent==None:
            self.root=n

    def traverse(self,n):
        temp = n
        if n.left != None:
            self.traverse(n.left)
        print(temp.key,end=" ")
        if n.right != None:
            self.traverse(n.right)



def main():
    t=BST()
    t.insert(5)
    t.insert(11)
    t.insert(35)
    t.insert(55)
    t.insert(65)
    t.insert(75)
    t.insert(2)
    t.insert(7)
    t.insert(9)
    print("searching 9")
    print(t.search(9))
    print("searching 500")

    print(t.search(500))
    print("minimum:")
    print(t.minimum(t.root).key)
    print("maximum:")

    print(t.maximum(t.root).key)
    t.traverse(t.root)
    print()
    print("deleting the root "+ str(t.root.key))
    t.delete(t.root)
    t.traverse(t.root)
    print()
    print("deleting the root "+ str(t.root.key))
    t.delete(t.root)
    t.traverse(t.root)
    print()
    


if __name__ == '__main__':
    main()