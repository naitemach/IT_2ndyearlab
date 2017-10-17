class TreeNode:
    def __init__(self, k=None):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None

    def minimum(self):
        temp = self
        while temp.left != None:
            temp = temp.left
        return temp

    def maximum(self):
        temp = self
        while temp.right != None:
            temp = temp.right
        return temp

    def isLeaf(self):
        if self.right == None and self.left == None:
            return True
        else:
            return False

    def predecessor(self):
        if self.left != None:
            return self.left.maximum()
        else:
            y = self.parent
            n = self
            while y.right != n and y != None:
                n = y
                y = y.parent
            return y

    def successor(self):
        if self.right != None:
            return self.right.minimum()
        else:
            n = self
            y = self.parent
            while y.left != n and y != None:
                n = y
                y = y.parent
            return y

    def getHeight(self):
        if self.isLeaf():
            return 1
        else:
            if self.left != None:
                lefth = self.left.getHeight()
            else:
                lefth = 0
            if self.right != None:
                righth = self.right.getHeight()
            else:
                righth = 0
            if lefth + 1 >= righth + 1:
                return lefth + 1
            else:
                return righth + 1

    def rotate(self, n):
        if n.left == self:
            n.left = self.right
            self.right = n
        else:
            n.right = self.left
            self.left = n
        if n.parent.left == n:
            n.parent.left = self
        else:
            n.parent.right = self
        self.parent = n.parent
        n.parent = self

    def isBalanced(self):
        if self.left != None and self.right != None:
            if abs(self.left.getHeight() - self.right.getHeight()) >= 2:
                return False
        if self.left == None and self.right != None:
            if abs(0 - self.right.getHeight()) >= 2:
                return False
        if self.left != None and self.right == None:
            if abs(self.left.getHeight() - 0) >= 2:
                return False
        if self.left != None:
            self.left.isBalanced()
        if self.right != None:
            self.right.isBalanced()
        return True

    def getZ(self):
        temp = self.parent
        if temp != None:
            if temp.isBalanced():
                temp = temp.parent
                temp.getZ()
            else:
                return temp

    def getY(self):
        temp = self
        if temp != None:
            if temp.parent.isBalanced():
                temp = temp.parent
                temp.getY()
            else:
                return temp

    def getX(self):
        temp = self
        if temp != None:
            if temp.parent.parent.isBalanced():
                temp = temp.parent
                temp.getX()
            else:
                return temp


class AvlTree:
    def __init__(self):
        self.root = TreeNode()

    def search(self, key):
        temp = self.root
        while temp != None:
            if key > temp.key:
                temp = temp.right
            elif key < temp.key:
                temp = temp.left
            elif key == temp.key:
                return True
        return False

    def insert(self, key):
        temp = self.root
        temp2 = TreeNode()
        temp2.key = key
        if temp.key == None:
            temp.key = key
        else:
            while True:
                if key > temp.key:
                    if temp.right == None:
                        temp.right = temp2
                        temp2.parent = temp
                        break
                    else:
                        temp = temp.right
                else:
                    if temp.left == None:
                        temp.left = temp2
                        temp2.parent=temp
                        break
                    else:
                        temp = temp.left
        if self.root.isBalanced():
            return
        else:
            z = temp2.getZ()
            y = temp2.getY()
            x = temp2.getX()
            if (z.left == y and y.left == x) or (z.right == y and y.right == x):
                y.rotate(z)
            elif (z.left == y and y.right == x) or (z.right == y and y.left == x):
                x.rotate(y)
                x.rotate(z)

    def traverse(self, n):
        temp = n
        if n.left !=gd None:
            self.traverse(n.left)
        print(temp.key, end=" ")
        if n.right != None:
            self.traverse(n.right)


def main():
    t = AvlTree()
    t.insert(5)
    t.insert(11)
    t.insert(35)
    t.insert(55)
    t.insert(65)
    t.insert(75)
    t.insert(2)
    t.insert(7)
    t.insert(9)
    t.traverse(t.root)
    print()


main()
