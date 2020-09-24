def change(num,n):
    isneg=num<0
    ans=""
    num=abs(num)
    while num!=0:
        tail=num%n
        if tail>9:
            tail=chr(64+tail-9)
        ans=str(tail)+' '+ans
        num//=n
    return ans if not isneg else '-'+ans

# print(change(-10,20))


class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#二叉树，判断镜像对称
def isvalid(l_child,r_child):
    if not l_child and  not r_child:return True
    if not l_child or not r_child:return False
    return l_child.val==r_child.val and isvalid(l_child.right,r_child.left) and isvalid(l_child.left,r_child.right)

#原来
root=TreeNode(3)
node1=TreeNode(1)
node2=TreeNode(1)
node3=TreeNode(2)
root.left=node1
root.right=node2
node2.right=node3
print(isvalid(root.left,root.right))
    