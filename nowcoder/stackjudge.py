# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack=[]
        i=0#pushV中的指针
        j=0#popV中的指针s
        while j<len(popV):
            if not stack or stack[-1]!=popV[j]:
                if i>=len(pushV):return False
                stack.append(pushV[i])
                i+=1
                continue
            stack.pop()
            j+=1
        if i==j and j==len(popV) and not stack:return True
        return False

push=[1,2,3,4,5]
pop=[4,5,3,2,1]
s=Solution()
print(s.IsPopOrder(push,pop))