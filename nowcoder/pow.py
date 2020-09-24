
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base==0:return 0
        if exponent==0:return 1
        temp=base
        res=1
        i=1#已经乘到了多少次幂
        while i<=exponent:
            if i*2<=exponent:
                temp*=temp
                i*=2
            else:
                exponent-=i
                i=1
                res*=temp
                temp=base
        return res
# s="ab"
# p="c*a*b"
t=Solution()
print (t.Power(2,9))   