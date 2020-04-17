nm=input().split()
n,m=int(nm[0]),int(nm[1])
mapcity=[[0]*(n+1) for i in range(n+1)]
visited=[False]*(n+1)
def getMinTimes(v,mapcity):
    if m==0:return -1
    if mapcity[n][n]==0:return -1
    from collections import deque
    q=deque()
    res=0
    if not visited[i]:
        q.append(v)
        visited[v]=True
    while q:
        t=q.popleft()
        for i in range(n):
            if mapcity[t][i] and not visited[i]:
                

    return 1
    

for i in range(m):
    uvx=list(map(lambda x: int(x),input().split()))
    u,v,x=uvx[0],uvx[1],uvx[2]
    mapcity[u][v]=x
print(getMinTimes(n,m,mapcity))
