import collections
class Solution:
    def calculate(self, s: str) -> int:
        ops=collections.deque()
        nums=collections.deque()
        i=0
        num=0
        while i<len(s):
            if s[i].isdigit():
                num=num*10+int(s[i])
            if s[i] in {'+','-','*','/'} or i==len(s)-1:
                nums.append(num)
                while ops and ops[-1] in {'*','/'}:
                    if ops[-1]=='*':
                        ops.pop()
                        x1=nums.pop()
                        x2=nums.pop()
                        nums.append(x1*x2)
                    elif ops[-1]=='/':
                        ops.pop()
                        x1=nums.pop()
                        x2=nums.pop()
                        nums.append(x2//x1)
                if i!=len(s)-1:
                    ops.append(s[i])
                num=0
            i+=1
        while ops:
            if ops[-1]=='+':
                ops.pop()
                x1=nums.pop()
                x2=nums.pop()
                nums.append(x2+x1)
            elif ops[-1]=='-':
                ops.pop()
                x1=nums.pop()
                x2=nums.pop()
                nums.append(x2-x1)
        return nums[0]
s="1-1+1"
print(Solution().calculate(s))