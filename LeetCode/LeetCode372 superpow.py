# class Solution:
#     def pow10(self,x,n):
#         if n==0:return 1
#         i=2 #下一步要计算到的次数
#         temp=x#辅助计算
#         res=1
#         while i<=n:
#             temp*=temp
#             if i*2<n:i*=2
#             else:
#                 n=n-i
#                 i=2
#                 res*=temp
#                 temp=x
#         if n==1:res*=x
#         return res%1337
#     def superPow(self, a: int, b) -> int:
#         res=self.pow10(a,b[-1])
#         #从倒数第二位开始遍历
#         temp=a
#         for i in range(len(b)-2,-1,-1):
#             temp=self.pow10(temp,10)
#             res*=self.pow10(temp,b[i])
#         return res%1337
#--------------------------------------------------

class Solution:
    def pow10(self,x,n):
        if n==0:return 1
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
        return res%1337
    def superPow(self, a: int, b) -> int:
        res=self.pow10(a,b[-1])
        #从倒数第二位开始遍历
        temp=a
        for i in range(len(b)-2,-1,-1):
            temp=pow(temp,10)%1337
            res*=pow(temp,b[i])%1337
        return res%1337
a = 2
b = [3]
t=Solution()
print (t.superPow(a,b))