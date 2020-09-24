t=int(input())
for i in range(t):
    nmab=input().split()
    n,m,a,b=int(nmab[0]),int(nmab[1]),int(nmab[2]),int(nmab[3])
    print(m)
pq=PriorityQueue()
def getNum(n,m,a,b):
    for num in nums:
        pq.put((num,num))