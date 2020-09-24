a=input()
b=input()
import math

def area(a,b):
    b=b.split()
    i=len(b)-1
    for i in range(len(b)):
        b[i]=int(b[i])
    b.sort()
    res=0
    while i >=0:
        r1=b[i]
        r2=b[i-1] if i-1>=0 else 0
        res+=math.pi*(r1*r1-r2*r2)
        i-=2
    print("%.5f" % res)
area(a,b)