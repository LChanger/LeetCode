class Solution:
    def cutRope(self, number):
        # write code here
        dp=[1,1]
        for i in range(2,number+1):
            dp.append(i-1)
            for j in range(1,i):
                dp[i]=max(dp[i],dp[i-j]*j,(i-j)*j)
        return dp[-1]
s=Solution()
print(s.cutRope(4))