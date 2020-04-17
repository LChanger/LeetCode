a=input()
b=input()
import re
def replce(a,b):
    pre=''
    if a[0]=='-':
        a=a[1:]
        pre='-'
    b=b.split()
    n=len(b)
    for i in range(len(a)):
        num=int(a[i])
        if num>n:break
        temp=b[num-1]
        a=a[:i]+temp+a[i+1:]
    return pre+a
print(replce(a,b))