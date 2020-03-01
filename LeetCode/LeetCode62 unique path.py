# 思路，纸面上画一下每步的步骤
#dp dp[i][j]代表从（0,0）点到（i,j)点的所有走法
#dp[i][j]=dp[i-1][j]+dp[i][j-1] 发现当求第i行时，第i-2行根本用不到
#所以将二维数组改为一维数组 dp[i]=dp[i-1]+dp[i]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        dp=[1 for i in range(n)]
        for j in range(1,m):
            for i in range(1,n):
                dp[i]=dp[i-1]+dp[i]
        return dp[n-1]

t = Solution()
print(t.uniquePaths(7,3))
