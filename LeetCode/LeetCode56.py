#思路：分组异或
class Solution:
    def singleNumbers(self, nums):
        sum=0
        for n in nums:
            sum^=n
        div=1
        while sum&div==0:
            div=div<<1
        a,b=0,0
        for n in nums:
            if n&div==div:a=a^n
            else:b=b^n
        return [a,b]
s=Solution()
nums=[1,2,5,2]
print(s.singleNumbers(nums))