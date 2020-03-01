#题目描述：A message containing letters from A-Z is being encoded to numbers using the following mapping:
#思路：动态规划法 dp[i]=dp[i-1]+dp[i-2] 其中对i-2的情况要进行合法性检验
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        def valid(t):
            if 0<int(t)<=26 and t[0]!='0':return True
            return False
        if n==1:return 1 if valid(s) else 0
        dp0=1 if valid(s[0:2]) else 0
        dp1=1 if valid(s[0]) else 0
        num=dp1+dp0
        for i in range(1,len(s)):
            if valid(s[i:i+1]) and valid(s[i-1:i+1]):
                num=dp0+dp1
            elif valid(s[i:i+1]):
                num=dp1
            elif valid(s[i-1:i+1]):
                num=dp0
            else:
                return 0
            dp0=dp1
            dp1=num
        return num
nums ="226"
t = Solution()
print(t.numDecodings(nums))