# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.
# Definition for a binary tree node.
# 思路利用next指针，进行层次遍历，方法是：定义一个值记录刚扫描完层的最左结点，然后对该层进行层次遍历，对下一层进行连接
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return None
        leftest=root#记录刚扫描完层的最左值
        while leftest.left:
            cur=leftest
            while cur:
                cur.left.next=cur.right
                if cur.next!=None:cur.right.next=cur.next.left
                cur=cur.next
            leftest=leftest.left
        return root
            
        
        
t1=TreeNode(2147483647)
t2=TreeNode(2)
t3=TreeNode(4)
t1.left=t2
t1.right=t3
t = Solution()
print(t.connect(t1))