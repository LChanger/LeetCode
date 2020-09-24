# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) :
        res=[]
        #递归
        def reCur(start,end):
            if start>end:return [None]
            ans=[]
            for mid in range(start,end+1):
                left_list=reCur(start,mid-1)
                right_list=reCur(mid+1,end)
                for lx in left_list:
                    for ry in right_list:
                        root=TreeNode(mid)
                        root.left=lx
                        root.right=ry
                        ans.append(root)
            return ans
        res=reCur(1,n)
        return res

print(Solution().generateTrees(3))