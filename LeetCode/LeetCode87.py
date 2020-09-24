class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        #三维dp  dp[i][j][k]表示s1[i]与s2[j]开始长度为k的可匹配与否
        if len(s1)!=len(s2):
            return False
        dp=[[[False for k in range(len(s1)+1)] for j in range(len(s1))] for i in range(len(s2))]
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                dp[i][j][0]=True
                if s1[i]==s2[j]:dp[i][j][1]=True
        for i in range(len(s1)-1,-1,-1):
            for j in range(len(s2)-1,-1,-1):
                for k in range(2,min(len(s1)-i,len(s2)-j)+1):
                    for cd in range(1,k):
                        dp[i][j][k]|=dp[i][j][cd] and dp[i+cd][j+cd][k-cd] or dp[i][j+k-cd][cd] and dp[i+cd][j][k-cd]
                        if dp[i][j][k]:break
        return dp

s1="abc"
s2="cba"
print(Solution().isScramble(s1,s2))