# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2:return False
        if not pRoot1:return False
        def curJudgesubtree(root1,root2):
            if not root2:return True
            if not root1 and root2:return False
            if root1 and root2 and root1.val==root2.val:
                return curJudgesubtree(root1.left,root2.left)&curJudgesubtree(root1.right,root2.right)
            return False
        #前序遍历
        stack=[pRoot1]
        while stack:
            top=stack.pop()
            if curJudgesubtree(top,pRoot2):return True
            if top.right:stack.append(top.right)
            if top.left:stack.append(top.left)
        return False
t=ListNode(1)
t2=ListNode(2)
t3=ListNode(3)
t.next=t2
t2.next=t3
s=Solution()
print (s.ReverseList(t))   