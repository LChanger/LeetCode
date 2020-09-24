# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 中序遍历：记录一个栈，将根入栈
# 1.如果栈不为空且栈顶元素左子节点存在则将左子节点入栈，直至左子节点为空
# 2.访问左子节点：如果栈不为空且栈顶元素右子节点不存在则访问左子节并弹栈
# 3.当右子节点存在，则取出栈顶节点（此为中序节点）访问，并将右子节点入栈，重复第一步
class Solution:
    def inorderTraversal(self, root):
        res=[]
        if not root:return []
        stack=[root]
        while stack:
            while stack and stack[-1].left:stack.append(stack[-1].left)
            while stack and not stack[-1].right:res.append(stack.pop().val)
            if not stack:return res
            temp=stack.pop()
            res.append(temp.val)
            stack.append(temp.right)
        return res
nums ="226"
t = Solution()
print(t.inorderTraversal(nums))