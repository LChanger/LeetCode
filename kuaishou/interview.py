#coding=utf-8
import sys 
#str = input()
#print(str)
print('Hello,World!')
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def visit(root):
    if not root:return None
    cur=root
    stack=[]
    res=[]
    while cur or stack:
        while cur:
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        res.append(cur.val)
        cur=cur.right
    root2=TreeNode(res[-1])
    p=root2
    for i in range(len(res)-2,-1,-1):
        node=TreeNode(res[i])
        p.right=node
        p=node
    return root2

def visit2(root):
    if not root:return None
    cur=root
    stack=[]
    res=[]
    while cur or stack:
        while cur:
            stack.append(cur)
            cur=cur.left
        cur=stack.pop()
        res.append(cur)
        cur=cur.right
    root2=res[-1]
    root2.left=None
    p=root2
    for i in range(len(res)-2,-1,-1):
        p.right=res[i]
        p=p.right 
        p.left=None
    return root2
n1=TreeNode(8)
n2=TreeNode(6)
n3=TreeNode(10)
n4=TreeNode(5)
n5=TreeNode(7)
n6=TreeNode(9)
n7=TreeNode(11)
n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n3.right=n7
print(visit2(n1))

