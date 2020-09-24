# 思路，折半查找 找小于等于根号x的最大值
class Solution:
    def mySqrt(self, x: int) -> int:
        low=1
        hi=x
        while low<hi:
            #此处为使为了取mid的高位，防止进入死循环
            mid=int((low+hi+1)/2)
            # 此处可以去掉 ==号判断， 将其加入 <= 的判断中 但是这样就会增加判断的次数 
            if mid*mid==x:return mid
            if mid*mid<=x:
                low=mid
                continue
            hi=mid-1
        return low
t = Solution()
print(t.mySqrt(8))
