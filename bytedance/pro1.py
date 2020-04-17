t=int(input())
def judge(a,b):
    if len(a)==0 and len(b)!=0:return "NO"
    if len(a)!=0 and len(b)==0:return "NO"
    if len(a)==0 and len(b)==0:return "YES"
    count=0
    pre=a[0]-b[0]
    c=[0]*len(a)
    for i in range(1,len(a)):
        c[i]=a[i]-b[i]
        if c[i]!=pre:
            pre=c[i]
            if pre!=0:count+=1
        if count>=2:return "NO"
    return "YES"
for i in range(t):
    n=input()
    a=list(map(lambda x: int(x),input().split()))
    b=list(map(lambda x: int(x),input().split()))
    print(judge(a,b))