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
# 空间复杂度O(1)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue1=[]
        queue2=[]
        if not root:return []
        queue1.append(root)
        res=[]
        res.append(queue1)
        while queue1!=[] or queue2!=[]:
            if queue1!=[]:
                while queue1:
                    temp=queue1[0]
                    del queue1[0]
                    if temp.left!=None:queue2.append(temp.left)
                    if temp.right!=None:queue2.append(temp.right)
                if queue2!=[]:
                    temp=[queue2[i] for i in range(len(queue2))]
                    res.append(temp)
            if queue2!=[]:
                while queue2!=[]:
                    temp=queue2[0]
                    del queue2[0]
                    if temp.left!=None:queue1.append(temp.left)
                    if temp.right!=None:queue1.append(temp.right)
                if queue1!=[]:
                    temp=[queue2[i] for i in range(len(queue2))]
                    res.append(queue1)
        return res
        
        
t1=TreeNode(2147483647)
t2=TreeNode(2)
t3=TreeNode(4)
t1.left=t2
t1.right=t3
t = Solution()
print(t.levelOrder(t1))