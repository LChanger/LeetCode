# 题目描述：Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
# 思路：维护两个队列进行层序遍历即可
# 记录最大数量
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 时间复杂度O(n)
# 空间复杂度O(logn)
# 采用层序遍历，用一个变量来记录该层共有几个结点
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        queue=[]
        queue.append(root)
        dep=0
        while queue:
            i=0
            layer=len(queue)
            while i<layer:
                temp=queue[0]
                del queue[0]#出队列
                if temp.left:queue.append(temp.left)
                if temp.right:queue.append(temp.right)
                i+=1
            dep+=1#dep 记录此时已经遍历完的层数
        return dep
            
        
        
t1=TreeNode(2147483647)
t2=TreeNode(2)
t3=TreeNode(4)
t1.left=t2
t1.right=t3
t = Solution()
print(t.maxDepth(t1))