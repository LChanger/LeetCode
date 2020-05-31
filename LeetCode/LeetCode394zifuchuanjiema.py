#思路：递归方式来做
class Solution:
    def decodeString(self, s: str) -> str:
        def recurSandL(s):
            if not s:return s,0
            num=0
            res=''
            cnt_left=0
            i=0
            while i<len(s):
                if s[i]=='[':
                    cnt_left+=1
                    tmp,leng=recurSandL(s[i+1:])
                    if num in {0,1}:
                        res+=tmp
                        i+=leng
                    else:
                        res+=num*tmp
                        i+=leng
                    cnt_left-=1
                    num=0
                elif s[i].isdigit():
                    num=num*10+int(s[i])
                elif s[i]==']' and cnt_left==0:
                    return res,i+1
                else:
                    res+=s[i]
                i+=1
            return res,i
        res,_=recurSandL(s)
        return res
s="3[a]2[bc]"
print(Solution().decodeString(s))