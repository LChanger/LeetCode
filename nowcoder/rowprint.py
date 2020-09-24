# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:return []
        from collections import deque
        que=deque()
        que.append(pRoot)
        res=[]
        while que:
            res.append([que[i].val for i in range(len(que))])
            layer=len(que)
            while layer>0:
                top=que.popleft()
                if top.left:que.append(top.left)
                if top.right:que.append(top.right)
                layer-=1
        return res
n1=TreeNode(8)
n2=TreeNode(6)
n3=TreeNode(10)
n4=TreeNode(5)
n5=TreeNode(7)
n6=TreeNode(9)
n7=TreeNode(11)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
t=Solution()
print (t.Print(n1))  