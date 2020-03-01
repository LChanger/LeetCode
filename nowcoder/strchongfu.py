# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    words=[0]*58
    s=''
    def FirstAppearingOnce(self):
        # write code here
        for i in range(len(self.s)):
            if self.words[ord(self.s[i])-65]==1:return self.s[i]
        return '#'
    def Insert(self, char):
        # write code here
        self.s+=char
        self.words[ord(char)-65]+=1
s=Solution()
for c in 'gggle':
    s.Insert(c)
    print(s.FirstAppearingOnce())