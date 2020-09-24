#思路：试探 a和b的长度
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern and value:return False
        if not pattern and not value:return True
        a_times=0
        b_times=0

        for i in range(len(pattern)):
            if pattern[i]=='a':a_times+=1
            else: b_times+=1
        if a_times==0 or b_times==0:
            l=len(value)//max(a_times,b_times)
            if not l:return True
            temp=value[:l]
            for i in range(l,len(value),l):
                if value[i:i+l]!=temp:return False
            return True
        #测试a的长度
        max_a=len(value)//a_times
        for al in range(0,max_a+1):
            bl=(len(value)-al*a_times)//b_times
            start=0
            a=''
            b=''
            for p in pattern:
                if p=='a':
                    temp=value[start:start+al]
                    if a=='':
                        a=temp
                    elif a!=temp:
                        break
                    start+=al
                elif p=='b':
                    temp=value[start:start+bl]
                    if b=='':
                        b=temp
                    elif b!=temp:
                        break
                    start+=bl
            if start==len(value) and a!=b:return True
        return False
pattern="bbbaa"
value="xxxxxxy"
print(Solution().patternMatching(pattern,value))