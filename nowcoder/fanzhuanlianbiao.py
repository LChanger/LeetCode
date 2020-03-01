# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:return None
        pre=pHead
        pn=pre.next
        while pn!=None:
            temp=pn.next
            pn.next=pre
            pre=pn
            pn=temp
        return pre
t=ListNode(1)
t2=ListNode(2)
t3=ListNode(3)
t.next=t2
t2.next=t3
s=Solution()
print (s.ReverseList(t))   