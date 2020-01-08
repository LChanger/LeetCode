class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:return 1
        neg=n<0
        n=abs(n)
        i=2 #下一步要计算到的次数
        temp=x#辅助计算
        res=1
        while i<=n:
            temp*=temp
            if i*2<n:i*=2
            else:
                n=n-i
                i=2
                res*=temp
                temp=x
        if n==1:res*=x
        return res if not neg else 1/res
c,n=2.00000, -2
t=Solution()
print (t.myPow(c,n))