T=int(input())
nk=input().split()
n,k=int(nk[0]),int(nk[1])
def get(n,k,grid):
    def dfs(i,j,val):
        if i<0 or i>=n or j<0 or j>=n or visited[i][j] or grid[i][j]<=val:return 0
        maxValueA=0
        maxValueB=0
        maxValueC=0
        maxValueD=0
        visited[i][j]=True
        for kk in range(1,k+1):
            a=dfs(i-kk,j,grid[i][j])
            maxValueA=max(maxValueA,a)
            # b=dfs(i+k,j,grid[i][j])
            # c=dfs(i,j-k,grid[i][j])
            # d=dfs(i,j+k,grid[i][j])
            # maxtemp=max(d,max(c,max(a,b)))
            # if maxtemp>maxValue:maxValue=maxtemp
        for kk in range(1,k+1):
            b=dfs(i+kk,j,grid[i][j])
            maxValueB=max(maxValueB,b)
        for kk in range(1,k+1):
            c=dfs(i,j-kk,grid[i][j])
            maxValueC=max(maxValueC,c)
        for kk in range(1,k+1):
            d=dfs(i,j+kk,grid[i][j])
            maxValueD=max(maxValueD,d)
        visited[i][j]=False
        maxValue=max(maxValueA,max(maxValueB,max(maxValueC,maxValueD)))
        return maxValue+grid[i][j]
    visited=[[False]*n for i in range(n)]
    return dfs(0,0,0)
for t in range(T):
    grid=[]
    for i in range(n):
        grid.append(list(map(lambda x:int(x),input().split())))
    print(get(n,k,grid))

