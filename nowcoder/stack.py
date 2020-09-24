# -*- coding:utf-8 -*-
class Solution:
    stack=[]
    minval=[]
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minval:
            self.stack.append(node)
            return node
        for i in range(len(self.minval)):
            if node<self.minval[i]:
                self.minval.insert(i,node)
                return node
        self.minval.insert(i+1,node)
        return node
    def pop(self):
        # write code here
        if not self.stack:return None
        top=self.stack.pop()
        index=self.minval.index(top)
        del self.minval[index]
        return top
    def top(self):
        # write code here
        if not self.stack:return None
        return self.stack[-1]
    def min(self):
        # write code here
        if not self.stack:return None
        return self.minval[0]

s=Solution()
print (s.push(3))   
print (s.min())  
print (s.push(4))   
print (s.min())  