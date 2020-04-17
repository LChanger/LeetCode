#思路：动态规划
#dp[i][j]代表text1[:i]到text2[:j]的最长公共子序列长度
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 
        n1,n2=len(text1),len(text2)
        dp=[[0 for j in range(n2+1)] for i in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:dp[i][j]=dp[i-1][j-1]+1
                else:dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]

class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:return 
        n1,n2=len(text1),len(text2)
        dp=[0 for j in range(n2+1)]
        for i in range(1,n1+1):
            pre=dp[0]
            for j in range(1,n2+1):
                temp=dp[j]
                dp[j]=pre+1 if text1[i-1]==text2[j-1] else max(dp[j],dp[j-1])
                pre=temp
        return dp
word1="sea"
word2="ate"
s=Solution1()
print(s.longestCommonSubsequence(word1,word2))