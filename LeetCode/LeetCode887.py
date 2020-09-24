#思路：肯定是动态规划 dp[i][j]表示第i层楼j个鸡蛋的最小次数 dp[i][j]=min(max(dp[A-1][j-1],dp[n-A][j])+1)
#T:O(N^2)
#S:O(N)
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp=[[0]*(K+1) for i in range(N+1)]#dp[i][0]表示k-1个鸡蛋次数，dp[i][1]=k个鸡蛋次数
        for i in range(1,N+1):
            dp[i][1]=i
            for j in range(2,K+1):
                temp_min=i
                for a in range(1,i):
                    temp=max(dp[a-1][j-1],dp[i-a][j])+1
                    if temp<temp_min:
                        temp_min=temp
                dp[i][j]=temp_min
        return dp[-1][-1]
K=1
N=3
print(Solution().superEggDrop(K,N))