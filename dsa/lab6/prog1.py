class Tree:
    def __init__(self, x):
        self.key = x
        self.right_child = None
        self.left_child = None
        self.parent = None
        self.height = 0

class BinSearchTree:
    def __init__(self):
        self.root = Tree(None)

    def insert(self, x):
        temp = Tree(x)
        if self.root.key is None:
            self.root = temp
        else:
            temp1 = self.root
            parent = temp1.parent
            while temp1 is not None:
                if x <= temp1.key:
                    parent = temp1
                    temp1 = temp1.left_child
                else:
                    parent = temp1
                    temp1 = temp1.right_child
            if x <= parent.key:
                parent.left_child = temp
                temp.parent = parent
            else:
                parent.right_child = temp
                temp.parent = parent
        self.setHeight(self.root)
        Z = None
        Y = None
        X = None
        test = self.check(temp)
        if test is not None:
            Z = test
            X = temp.parent
            Y = temp.parent
            while Y is not None:
                if Y == Z.left_child:
                    break
                elif Y == Z.right_child:
                    break
                Y = Y.parent
            while X is not None and Y is not None:
                if Y.left_child is not None and X == Y.left_child:
                    break
                elif Y.right_child is not None and X == Y.right_child:
                    break
                X = X.parent
            if Y == Z.right_child and X == Y.right_child:
                Y.parent = Z.parent
                Z.right_child = Y.left_child
                if Y.left_child is not None:
                    Y.left_child.parent = Z
                Y.left_child = Z
                Z.parent = Y
            elif Y == Z.left_child and X == Y.left_child:
                Y.parent = Z.parent
                Z.left_child = Y.right_child
                if Y.right_child is not None:
                    Y.right_child.parent = Z
                Y.right_child = Z
                Z.parent = Y
            elif Y == Z.left_child and X == Y.right_child:
                X.parent = Z.parent
                if Z == Z.parent.left_child:
                    Z.parent.left_child = X
                if Z == Z.parent.right_child:
                    Z.parent.right_child = X
                Z.left_child = X.right_child
                X.right_child.parent = Z
                Y.right_child = X.left_child
                if X.left_child is not None:
                    X.left_child.parent = Y
                X.left_child = Y
                Y.parent = X
                X.right_child = Z
                Z.parent = X
            else:
                X.parent = Z.parent
                if Z == Z.parent.left_child:
                    Z.parent.left_child = X
                if Z == Z.parent.right_child:
                    Z.parent.right_child = X
                Z.right_child = X.left_child
                X.left_child.parent = Z
                Y.left_child = X.right_child
                if X.right_child is not None:
                    X.right_child.parent = Y
                X.right_child = Y
                Y.parent = X
                X.left_child = Z
                Z.parent = X

    def check(self, temp):
        temp = temp.parent
        while temp is not None:
            if temp.left_child is not None and temp.right_child is not None:
                if temp.left_child.height - temp.right_child.height > 1:
                    return temp
                elif temp.right_child.height - temp.left_child.height > 1:
                    return temp
            temp = temp.parent
        return

    def printTree(self, temp):
        if temp.key is None:
            return
        else:
            print(temp.key)
            # print (temp.height)
            if temp.left_child is not None:
                self.printTree(temp.left_child)
            if temp.right_child is not None:
                self.printTree(temp.right_child)

    def search(self, x):
        temp = self.root
        flag = 0
        while temp is not None:
            if temp.key == x:
                flag = 1
                break
            if x < temp.key:
                temp = temp.left_child
            elif x > temp.key:
                temp = temp.right_child
        if flag == 1:
            return 1
        else:
            return 0

    def minimum(self):
        temp = self.root
        parent = temp.parent
        while temp is not None:
            parent = temp
            temp = temp.left_child
        print(parent.key)

    def maximum(self):
        temp = self.root
        parent = temp.parent
        while temp is not None:
            parent = temp
            temp = temp.right_child
        print(parent.key)

    def successor(self, x):
        temp = self.root
        flag = 0
        while temp is not None:
            if temp.key == x:
                flag = 1
                break
            if x < temp.key:
                temp = temp.left_child
            else:
                temp = temp.right_child
        if flag == 0:
            print("No such node")
        else:
            # print (temp.key)
            if temp.right_child is not None:
                parent = temp
                temp = temp.right_child
                while temp is not None:
                    parent = temp
                    temp = temp.left_child
                return parent
            else:
                # print (temp.key)
                parentNode = temp.parent
                # print (parentNode.key)
                while parentNode is not None and temp == parentNode.right_child:
                    temp = parentNode
                    parentNode = parentNode.parent
                if parentNode is not None:
                    return parentNode
                else:
                    return None

    def predecessor(self, x):
        temp = self.root
        flag = 0
        while temp is not None:
            if temp.key == x:
                flag = 1
                break
            if x < temp.key:
                temp = temp.left_child
            else:
                temp = temp.right_child
        if flag == 0:
            print("No such node")
        else:
            if temp.left_child is not None:
                parent = temp
                temp = temp.left_child
                while temp is not None:
                    parent = temp
                    temp = temp.right_child
                return parent
            else:
                parentNode = temp.parent
                while parentNode is not None and temp == parentNode.left_child:
                    temp = parentNode
                    parentNode = parentNode.parent
                if parentNode is not None:
                    return parentNode
                else:
                    return None

    def delete(self, x):
        temp = self.root
        flag = 0
        while temp is not None:
            if temp.key == x:
                flag = 1
                break
            if x < temp.key:
                temp = temp.left_child
            else:
                temp = temp.right_child
        if flag == 0:
            print("No such node")
        else:
            parent = temp.parent
            mynode = temp
            parentMyNode = mynode.parent
            if temp.left_child is None and temp.right_child is None:
                if temp == temp.parent.left_child:
                    temp.parent.left_child = None
                else:
                    temp.parent.right_child = None
            elif temp.left_child is None and temp.right_child is not None:
                if temp == temp.parent.left_child:
                    temp.parent.left_child = temp.right_child
                else:
                    temp.parent.right_child = temp.right_child
            elif temp.left_child is not None and temp.right_child is None:
                if temp == temp.parent.left_child:
                    temp.parent.left_child = temp.left_child
                else:
                    temp.parent.right_child = temp.left_child
            else:
                pre = self.successor(x)
                self.delete(pre.key)
                temp.key = pre.key
                # print (pre.key)
            self.setHeight(self.root)
            # self.showHeight(self.root)
            Z = None
            Y = None
            X = None
            while True:
                if temp.parent is not None:
                    parent = temp.parent
                    mynode = temp
                    parentMyNode = mynode.parent
                    test = self.check(mynode.parent)
                    if test is not None:
                        Z = test
                        X = parentMyNode
                        Y = parentMyNode
                    # Z1 = Z.left_child
                    # Z2 = Z.right_child
                        while Y is not None:
                            if Y == Z.left_child:
                                break
                            elif Y == Z.right_child:
                                break
                            Y = Y.parent
                        if Y == Z.left_child:
                            Y = Z.right_child
                        else:
                            Y = Z.left_child
                        if Y.left_child is None:
                            X = Y.right_child
                        elif Y.right_child is None:
                            X = Y.left_child
                        if Y.left_child is not None and Y.right_child is not None and Y.left_child.height >= Y.right_child.height:
                            X = Y.left_child
                        else:
                            X = Y.right_child
                        if Y == Z.right_child and X == Y.right_child:
                            Y.parent = Z.parent
                            Z.right_child = Y.left_child
                            if Y.left_child is not None:
                                Y.left_child.parent = Z
                            Y.left_child = Z
                            Z.parent = Y
                        elif Y == Z.left_child and X == Y.left_child:
                            Y.parent = Z.parent
                            Z.left_child = Y.right_child
                            if Y.right_child is not None:
                                Y.right_child.parent = Z
                            Y.right_child = Z
                            Z.parent = Y
                        elif Y == Z.left_child and X == Y.right_child:
                            X.parent = Z.parent
                            if Z == Z.parent.left_child:
                                Z.parent.left_child = X
                            if Z == Z.parent.right_child:
                                Z.parent.right_child = X
                            Z.left_child = X.right_child
                            X.right_child.parent = Z
                            Y.right_child = X.left_child
                            if X.left_child is not None:
                                X.left_child.parent = Y
                            X.left_child = Y
                            Y.parent = X
                            X.right_child = Z
                            Z.parent = X
                        else:
                            X.parent = Z.parent
                            if Z == Z.parent.left_child:
                                Z.parent.left_child = X
                            if Z == Z.parent.right_child:
                                Z.parent.right_child = X
                            Z.right_child = X.left_child
                            X.left_child.parent = Z
                            Y.left_child = X.right_child
                            if X.right_child is not None:
                                X.right_child.parent = Y
                            X.right_child = Y
                            Y.parent = X
                            X.left_child = Z
                            Z.parent = X
                        temp = Z
                    else:
                        break
                else:
                    break


    def height(self, temp):
        if temp is None:
            return 0
        else:
            lh = self.height(temp.left_child)
            rh = self.height(temp.right_child)
            if lh < rh:
                return rh + 1
            else:
                return lh + 1

    def setHeight(self, temp):
        if temp is None:
            return
        else:
            self.setHeight(temp.left_child)
            self.setHeight(temp.right_child)
            if temp.left_child is None and temp.right_child is None:
                temp.height = 1
            elif temp.right_child is not None and temp.left_child is None:
                temp.height = temp.right_child.height + 1
            elif temp.left_child is not None and temp.right_child is None:
                temp.height = temp.left_child.height + 1
            elif temp.left_child is not None and temp.right_child is not None:
                temp.height = max(temp.left_child.height, temp.right_child.height) + 1

    def showHeight(self, temp):
        if temp is None:
            return
        else:
            print (temp.height)
            self.showHeight(temp.left_child)
            self.showHeight(temp.right_child)


B = BinSearchTree()
B.insert(10)
B.setHeight(B.root)
B.insert(5)
B.setHeight(B.root)
B.insert(2)
B.setHeight(B.root)
B.insert(8)
B.setHeight(B.root)
B.insert(15)
B.setHeight(B.root)
B.insert(14)
B.setHeight(B.root)
B.insert(16)
B.setHeight(B.root)
B.insert(7)
B.setHeight(B.root)
B.insert(6)
B.setHeight(B.root)

B.printTree(B.root)

if B.search(11):
    print ("Found")
else:
    print("Not found")
B.minimum()
B.maximum()
print ("Successor:")
succ = B.successor(14)
print (succ.key)
print ("Predecessor:")
pre = B.predecessor(10)
print (pre.key)
B.delete(5)
print ("After deleting:")
B.printTree(B.root)



