def postFix(s):
    l=[]
    for i in s:
       if i=="+":
           b=int(l.pop())
           a=int(l.pop())
           res=a+b
           l.append(res)
       elif i == "-":
           b = int(l.pop())
           a = int(l.pop())
           res = a - b
           l.append(res)
       elif i == "/":
           b = int(l.pop())
           a = int(l.pop())
           res = a/b
           l.append(res)
       elif i == "*":
           b = int(l.pop())
           a = int(l.pop())
           res = a*b
           l.append(res)
       else:
           l.append(i)
    return l.pop()
#e="10 12 + 10 -"
e=input("Enter the postfix expression: ")
s=e.split(' ')
fres=postFix(s)
print(fres)




