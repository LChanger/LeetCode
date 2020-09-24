# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        #有右节点
        if pNode.right:
            pNode=pNode.right
            while pNode.left:pNode=pNode.left
            return pNode
        #无右节点
        #为左子节点
        if pNode.next and pNode.next.left==pNode:
            return pNode.next
        #为右子节点
        if pNode.next and pNode.next.right==pNode:
            pNode=pNode.next
            pNode.right=None
            return self.GetNext(pNode)
        return None