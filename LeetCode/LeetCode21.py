# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=p=ListNode(0)
        while(l1!=None and l2!=None):
        	if l1.val<l2.val:
        		res=ListNode(l1.val)
        		p.next=res
        		p=res
        		l1=l1.next
        	else:
        		res=ListNode(l2.val)
        		p.next=res
        		p=res
        		l2=l2.next
        if l1!=None:p.next=l1
        else: p.next=l2
        return head.next

