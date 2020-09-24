# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:return None
        countMap={}
        def getNodeNum(root):
            if not root:return 0
            left=getNodeNum(root.left)
            right=getNodeNum(root.right)
            countMap[root.val]=[left,right]
            return left+right+1
        Num=getNodeNum(pRoot)
        def find(root,k):
            if not root:return None
            if countMap[root.val][0]==k-1:return root.val
            if countMap[root.val][0]>k-1:return find(root.left,k)
            if countMap[root.val][0]<k-1:return find(root.right,k-countMap[root.val][0]-1)
        return find(pRoot,k)
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
print (t.KthNode(n1,4))  