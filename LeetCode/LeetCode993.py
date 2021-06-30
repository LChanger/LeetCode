# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        que=collections.deque()
        que.append([root,None])
        while que:
            layer=len(que)
            isx=None
            x_p=None
            y_p=None
            isy=None
            while layer>0:
                top,parent=que.popleft()
                if top.val==x:
                    isx=top
                    x_p=parent
                if top.val==y:
                    isy=top
                    y_p=parent
                if top.left:
                    que.append([top.left,top])
                if top.right:
                    que.append([top.right,top])
                layer-=1
            if isx and isy and x_p!=y_p:
                return True
        return False
root=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
node3=TreeNode(4)
node4=TreeNode(5)
root.left=node1
root.right=node2
node1.right=node3
node2.right=node4
print(Solution().isCousins(root,4,5))
