import collections
class Solution:
    def calculate(self, s: str) -> int:
        ops=collections.deque()
        i=0
        sign=1
        ops.append(1)
        ret=0
        while i<len(s):
            if s[i]==' ':
                i+=1
            elif s[i]=='+':
                sign=ops[-1]
                i+=1
            elif s[i]=='-':
                sign=-ops[-1]
                i+=1
            elif s[i]=='(':
                ops.append(sign)
                i+=1
            elif s[i]==')':
                ops.pop()
                i+=1
            else:
                num=0
                while i<len(s) and s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1
                ret+=sign*num
        return ret
s=" 2-1 + 2 "
print(Solution().calculate(s))