class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word2=='':return len(word1)
        if word1=='':return len(word2)
        dp=[[0 for j in range(len(word2))] for i in range(len(word1))]
        dp[0][0]=0 if word1[0]==word2[0] else 1
        for j in range(1,len(word2)):
            if word1[0]==word2[j]:
                dp[0][j]=j
            else:
                dp[0][j]=dp[0][j-1]+1
        for i in range(1,len(word1)):
            if word1[i]==word2[0]:
                dp[i][0]=i
            else:
                dp[i][0]=dp[i-1][0]+1
        for i in range(1,len(word1)):
            for j in range(1,len(word2)):
                if word1[i]==word2[j]:
                    dp[i][j]=min(dp[i-1][j-1],min(dp[i][j-1]+1,dp[i-1][j]+1))
                else:
                    dp[i][j]=min(dp[i-1][j-1]+1,min(dp[i][j-1]+1,dp[i-1][j]+1))
        return dp

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        if word2=='':return len(word1)
        if word1=='':return len(word2)
        #dp[i][j]代表word1[:i]到word2[:j]的编辑距离
        n1=len(word1)
        n2=len(word2)
        dp=[[j-1 for j in range(n2+1)] for i in range(n1+1)]
        dp[0][0]=0
        for i in range(1,n1+1):
            dp[i][0]=i
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:dp[i][j]=dp[i-1][j-1]
                else:dp[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
        return dp
word1="sea"
word2="ate"
s=Solution1()
print(s.minDistance(word1,word2))