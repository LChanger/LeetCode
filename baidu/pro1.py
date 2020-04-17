n=input()
m=input()
a=input()
b=input()
def maxscore(a,b,n,m):
    a=a.split()
    b=b.split()
    n=int(n)
    m=int(m)
    for i in range(len(a)):
        a[i]=int(a[i])
        b[i]=int(b[i])
    a.insert(0,0)
    b.insert(0,0)
    for i in range(1,len(b)):
        for j in range(i,len(b)):
            if b[i]<b[j]:
                b[i],b[j]=b[j],b[i]
                a[i],a[j]=a[j],a[i]
    dp=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):dp[i][1]=a[i]
    for i in range(1,n+1):
        for j in range(1,min(m,i)+1):
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+a[i]-b[i]*(j-1))
    print(dp[n][m])
maxscore(a,b,n,m)
