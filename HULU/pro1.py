n=int(input())
nums=list(map(int,input().split()))
def get_types(nums):
    nums.sort()
    #dp[i][j]表示 dp[i:j]的种类数
    dp=[[1]*(n+1) for i in range(n+1)]
    #dp[i][j]=sum(dp[i][k]*dp[k+1][j])
    dp[n][n]=1
    for i in range(n-1,-1,-1):
        dp[i][i]=1
        dp[i][i+1]=1
        for j in range(i+2,n+1):
            sum=0
            k=i
            while k<j:
                if k>i and nums[k]!=nums[k-1] or k==i:
                    sum+=dp[i][k]*dp[k+1][j]
                k+=1
                
            dp[i][j]=sum%1000000007
    return dp[0][-1]
print(get_types(nums))

# n=int(input())
# nums=list(map(int,input().split()))
# def get_num_trees(n):
#     G=[0]*(n+1)
#     G[0]=1
#     G[1]=1
#     for i in range(2,n+1):
#         for j in range(1,i+1):
#             G[i]+=G[j-1]*G[i-j]
#     return G[-1]
# def factorial(number):
#     if number<=1:return 1
#     return number*factorial(number-1)
# def get_types(nums):
#     cache={}
#     for x in nums:
#         cache[x]=cache.get(x,0)+1
#     res=[]
#     for k in cache:
#         index=cache[k]
#         if index>=2:res.append(k)
#     total=get_num_trees(n)
#     for x in res:
#         total//=factorial(x)
#     return total%1000000007
# print(get_types(nums))



# n=int(input())
# nums=list(map(int,input().split()))
# xin_n=len(list(set(nums)))
# def get_types(nums):
#     #nums.sort()
#     G=[0]*(n+1)
#     G[0]=1
#     G[1]=1
#     for i in range(2,n+1):
#         for j in range(1,i+1):
#             G[i]+=G[j-1]*G[i-j]
#     return G[-1]
# print(get_types(nums))