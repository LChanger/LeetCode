#题目描述：A message containing letters from A-Z is being encoded to numbers using the following mapping:
#思路：动态规划法 dp[i]=dp[i-1]+dp[i-2] 其中对i-2  i-1 的情况要进行合法性检验
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        # 计算输入字符串（长度为1或2）所包含的情况
        def numcondition(t):
            if len(t)==1:
                if t=="*":return 9
                elif 0<int(t)<=26:return 1
                return 0
            # t为2字符
            if t.isdigit():
                if 9<int(t)<=26:return 1
                return 0
            if t=="**":return 15 # 11-19 21-26 单数情况
            # t[0]=="*" t[1]!="*"
            if t[0]=="*":
                if int(t[1])<=6:return 2 # *可为1,2
                return 1  #“*”只能为1
            #t[1]=="*" t[0]!="*"
            if int(t[0])==1:return 9   # 11-19 
            if int(t[0])==2:return 6  #21-26
            return 0

        if n==1:return numcondition(s)
        dp0=numcondition(s[0])
        dp1=numcondition(s[0:2])
        num=dp1+dp0*numcondition(s[1])
        for i in range(2,len(s)):
            num=dp0*(numcondition(s[i-1:i+1]))+num*numcondition(s[i:i+1])
            if num==0:return 0
            dp0=dp1
            dp1=num
        return num%(pow(10,9)+7)
nums ="1*"
t = Solution()
print(t.numDecodings(nums))