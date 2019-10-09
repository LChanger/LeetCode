# Definition for singly-linked list.
s ="aaa"
words = ["aa","aa"]

# 思路，纸面上画一下每步的步骤
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        intMax, intMin = 2147483647, -2147483648
        isnegative=(dividend<0)^(divisor<0)
        dividend,divisor=abs(dividend),abs(divisor)
        res=0
        while dividend>=divisor:
            tmp,val=divisor,1
            while dividend>=tmp:
                res+=val
                dividend-=tmp
                tmp<<=1
                val<<=1
        if isnegative:
            res=-res
            return max(res,intMin)
        return min(res,intMax)

#参考思路 https://www.cnblogs.com/grandyang/p/4521224.html
t = Solution()
print(t.divide(-7,3))
