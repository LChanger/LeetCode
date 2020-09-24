#思路：可以抽象为背包问题，dp[i][j] 给定i个0和j个1的所拼最大数量
#本质上是 dp[i][j][k]表前k个元素，dp[i][j][k]=max(dp[i-a][j-b][k-1]+1)
#化简dp[i][j]=max(dp[i-a][j-b]+1)  a,b=strs[i]的0和1数量
#T:O(mnk)
#S:O(mn+k)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n:  int) -> int:
        count=[]
        dp=[[0]*(n+1) for i in range(m+1)]
        for k in range(len(strs)):
            c0,c1=strs[k].count('0'),strs[k].count('1') 
            #此处必须倒序遍历，否则会存在重复计数的情况
            for i in range(m,c0-1,-1):
                for j in range(n,c1-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-c0][j-c1]+1)
        return dp[-1][-1]
array=["10","0001","111001"]
m=5
n=3
s=Solution()
print(s.findMaxForm(array,m,n))