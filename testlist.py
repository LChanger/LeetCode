
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
res=[]
res.append(TreeNode(10))
print(res[0].val)
res[0].val=100
print(res[0].val)