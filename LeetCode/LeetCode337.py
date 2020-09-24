class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:return 0
        def recurMax(node):#返回两个值，子树的最大值和包含子节点的最大值
            if not node:return 0,0
            leftmax,leftchildmax=recurMax(node.left)
            rightmax,rightchildmax=recurMax(node.right)
            return max(leftmax+rightmax,leftchildmax+rightchildmax+node.val),leftmax+rightmax
        res,_=recurMax(root)
        return res
t1=TreeNode(3)
t2=TreeNode(2)
t3=TreeNode(3)
t4=TreeNode(3)
t1.left=t2
t1.right=t3
t2.right=t4
s = Solution()
print(s.rob(t1))