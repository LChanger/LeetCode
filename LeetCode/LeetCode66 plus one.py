# 思路，纸面上画一下每步的步骤
#dp dp[i][j]代表从（0,0）点到（i,j)点的所有走法
#dp[i][j]=dp[i-1][j]+dp[i][j-1] 发现当求第i行时，第i-2行根本用不到
#所以将二维数组改为一维数组 dp[i]=dp[i-1]+dp[i]
class Solution:
    def plusOne(self, digits):
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                break
            digits[i]=0
        if digits[0]==0:digits.insert(0,1)
        return digits
t = Solution()
d=[9]
print(t.plusOne(d))
