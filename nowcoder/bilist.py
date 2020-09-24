# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:return None
        def recur(root,isleft):
            if not root.left and not root.right:return root
            pre=nex=None
            if root.left:
                pre=recur(root.left,True)
                pre.right=root
                root.left=pre
            if root.right:
                nex=recur(root.right,False)
                root.right=nex
                nex.left=root
            if isleft:
                if nex:return nex
                return root
            if pre:return pre
            return root
        p=recur(pRootOfTree,False)
        while p.left:p=p.left
        return p
t1=TreeNode(10)
t2=TreeNode(6)
t3=TreeNode(4)
t4=TreeNode(8)
t5=TreeNode(5)
t1.left=t2
t2.left=t3
t2.right=t4
# t3.next=t4
# t4.next=t5
# t1.random=t3
# t2.random=t5
# t4.random=t2
s=Solution()
print (s.Convert(t1))   