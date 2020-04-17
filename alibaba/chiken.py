nmk=input().split()
temp=list(map(lambda x:int(x),nmk))
n,m,k=temp[0],temp[1],temp[2]
from queue import PriorityQueue
pq=PriorityQueue()
nums=input().split()
nums=map(lambda x:int(x),nums)
for num in nums:
    pq.put((num*-1,num))
for i in range(m):
    temp=[]
    for i in range(pq.qsize()):
        p,v=pq.get()
        v+=k
        p=v*-1
        temp.append((p,v))
    for i in range(len(temp)):
        pq.put(temp.pop())
    p,v=pq.get()
    v=v//2
    p=v*-1
    pq.put((p,v))
res=0
for i in range(pq.qsize()):
    res+=pq.get()[1]
print(res)
