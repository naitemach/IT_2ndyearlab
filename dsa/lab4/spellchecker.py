class hash:

    def __init__(self):
        self.T = [None for i in range(30)]

    def hashval(self,S):
        l = len(S) - 1
        sum = ord(S[l])
        l -= 1
        while l >= 0 :
            sum = ord(S[l]) + 33*sum
            l -= 1
        return sum
    
    def insert(self,key):
        val = self.hashval(key)
        pos = val % 30
        l = ListNode(val,None,key)
        if self.T[pos] == None:
            self.T[pos] = l
        else :
            ptr = self.T[pos]
            l.next = ptr
            self.T[pos] = l

    def search(self,key):
        val = self.hashval(key)
        pos = val % 30
        ptr = self.T[pos]
        if ptr == None:
            return False
        else :
            while ptr != None:
                if key == ptr.key:
                    return True
                else :
                    ptr = ptr.next
            return False

    def delete(self,key):
        val = self.hashval(key)
        pos = val % 30
        ptr = self.T[pos]
        if ptr == None:
            print('Element not present')
            return
        if ptr.key == key :
            self.T[pos] = ptr.next
            print('deleted')
            return
        while ptr.next != None :
            if  key == ptr.next.key:
                ptr.next = ptr.next.next
                print('Deleted')
                break
            else:
                ptr = ptr.next
        print('Element not present')

    def keys(self):
        for i in self.T :
            if i != None:
                ptr = i
                while ptr != None:
                    print(ptr.key)
                    ptr = ptr.next

class ListNode:
    def __init__(self,val=None,nxt=None,key=None):
        self.value=val
        self.next=nxt
        self.key=key

def main():
    H = hash()
    with open('small.dict','r') as f:
        for line in f:
            word = line.split('\n')
            H.insert(word[0])
    key = input('Enter the key :')
    print(H.search(key))

        
if __name__ == '__main__':
    main()