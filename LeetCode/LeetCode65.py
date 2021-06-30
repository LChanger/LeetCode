class Solution:
    def isNumber(self, s: str) -> bool:
        start=0
        if not s[0].isdigit():
            if s[0] not in {'+','-','.'}:
                return False
            start=1
        xiaoshudian=1
        letter=1
        digit=0
        for i in range(start,len(s)):
            if not s[i].isdigit():
                if xiaoshudian<0 or letter<0:
                    return False
                if s[i]=='.':
                    xiaoshudian-=1
                    if not s[i+1:i+2].isdigit() and not s[i-1:i].isdigit():
                        return False
                elif s[i] in {'e','E'}:
                    letter-=1
                else:
                    return False
            else:
                digit+=1
        return True if digit>0 else False
t = Solution()
d='3.'
print(t.isNumber(d))
