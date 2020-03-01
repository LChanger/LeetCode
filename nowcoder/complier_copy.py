# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:return None
        cur=pHead
        while cur:
            q=RandomListNode(cur.label)
            q.next=cur.next
            cur.next=q
            cur=q.next 
        cur=pHead
        while cur:
            cur.next.random=cur.random.next if cur.random else None
            cur=cur.next.next
        cur=pHead.next
        while cur:
            cur.next=cur.next.next if cur.next else None
            cur=cur.next
        return pHead.next

t1=RandomListNode(1)
t2=RandomListNode(2)
t3=RandomListNode(3)
t4=RandomListNode(4)
t5=RandomListNode(5)
t1.next=t2
t2.next=t3
t3.next=t4
t4.next=t5
t1.random=t3
t2.random=t5
t4.random=t2
s=Solution()
print (s.Clone(t1))   