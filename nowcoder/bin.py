class Solution:
    def NumberOf1(self, n):
        # write code here
        # 二进制转十进制  短除法
        if n==0:return 0
        count=0
        while n!=0:
            temp=n-1
            n=n & temp
            count+=1
        return count
# -*- coding:utf-8 -*-
# s="ab"
# p="c*a*b"
n=-9
t=Solution()
print (t.NumberOf1(n))   