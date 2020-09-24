# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:return False
        res=[]
        def recurFind(root,path,target):
            if target==root.val:
                if not root.left and not root.right:
                    res.append(path+[root])
                return
            if root.left:recurFind(root.left,path+[root],target-root.val)
            if root.right:recurFind(root.right,path+[root],target-root.val)
        
        recurFind(root,[],expectNumber)
        res.sort(key=lambda lis:len(lis),reverse=True)
        return res
n1=TreeNode(10)
n2=TreeNode(10)
n3=TreeNode(1)
n1.left=n2
n1.right=n3
t=Solution()
print (t.FindPath(n1,20))   