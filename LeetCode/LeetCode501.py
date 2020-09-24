#题目描述：Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
# 思路：由题意可知，相同的值只可能存在于父子节点之间，所以对树进行中序遍历
# 记录最大数量
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 时间复杂度O(n)
# 空间复杂度O(1)
maxcount=0 #记录目前最频繁项集的次数
preval=None
count=1#记录目前遍历值的个数,默认为1
class Solution:
    def findMode(self, root: TreeNode):
        res=[]#结果
        def traversal(node):
            global preval,maxcount,count
            if node==None:return
            traversal(node.left)
            if preval!=None: #不是遍历的起点
                if preval==node.val:
                    count+=1
                else:
                    count=1
            if count>maxcount:
                maxcount=count
                res.clear()
                res.append(node.val)
            elif count==maxcount:
                res.append(node.val)
            preval=node.val
            traversal(node.right)
        traversal(root)
        return res
#----------------------------------------------------------
class Solution2:
    prev = None
    max_count = 0
    current_count = 0 
    result = []

    def findMode(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.current_count = 1 if node.val != self.prev else self.current_count + 1
        if self.current_count == self.max_count:
            self.result.append(node.val)
        elif self.current_count > self.max_count:
            self.result = [node.val]
            self.max_count = self.current_count
        self.prev = node.val
        self.dfs(node.right)

t1=TreeNode(2147483647)
t2=TreeNode(2)
t3=TreeNode(4)
# t1.left=t2
# t1.right=t3
t = Solution()
print(t.findMode(t1))