class LinkedList:   
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head=ListNode()
        
    
    def insert(self,x,p):
        """Insert element x in the position after p"""
        temp=ListNode()
        temp.value=x
        temp.next=p.next
        p.next=temp 


    def delete(self,p):
        """Delete the node following node p in the linked list."""
        p.next=p.next.next
        

    def printlist(self):
        """ Print all the elements of a list in a row."""
        temp=self.head.next
        while temp!=None:
            print(temp.value,end=',')
            temp=temp.next
        print()

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp=self.head
        pos=-1
        while pos<i-1:
            if temp.next==None:
                break
            temp=temp.next
            pos=pos+1
        temp2=ListNode()
        temp2.value=x
        if temp.next!=None:
            temp2.next=temp.next
        temp.next=temp2
            
    def search(self,x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp=self.head.next
        while temp!=None:
            if temp.value==k:
                return temp
            else:
                temp=temp.next
        return None

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        temp=self.head.next
        sum=0
        while temp!=None:
            sum=sum+1
            temp=temp.next
        return sum

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        temp=self.head.next
        if temp==None:
            return True
        else:
            return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=0
        self.next=None

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is:',end='')
    L.printlist()
    L.insert(12,L.head.next)
    print('List is: ',end='')
    L.printlist()
    L.insert(2,L.head)
    print('List is: ',end='')
    L.printlist()
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ',end='')
    L.printlist()
    L.delete(L.head.next)
    print('List is: ',end='')
    L.printlist()
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ',end='')
    L.printlist()

if __name__ == '__main__':
    main()