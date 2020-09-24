#思路：动态规划  dp[j]表示以j-1为结尾的最长有效括号子串长度
class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        for i in range(1,len(s)):
            if s[i]=='(':dp[i+1]=0
            else:
                if s[i-1-dp[i]]=='(':
                    dp[i+1]=dp[i]+2+dp[i-1-dp[i]]
        return max(dp)

#思路：动态规划  dp[j]表示以j为结尾的最长有效括号子串长度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0]*len(s)
        for i in range(1,len(s)):
            if s[i]=='(':dp[i]=0
            else:
                if i-1-dp[i-1]>=0 and s[i-1-dp[i-1]]=='(':
                    dp[i]=dp[i-1]+2
                    if i-1-dp[i-1]-1>=0:
                        dp[i]+=dp[i-1-dp[i-1]-1]
        return max(dp)
s="(()))())("
print(Solution().longestValidParentheses(s))