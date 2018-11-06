# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Listpoint:
    def __init__(self, x):
        self.point = x
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list1=[]
        p=head
        while(p!=None):
        	pt=Listpoint(p)
        	list1.append(pt)
        	p=p.next
        dele=len(list1)-n
        if n==1:
        	if n==len(list1):return None
        	p=list1[dele-1].point
        	p.next=None
        	return head
        elif n==len(list1):
        	return list1[dele+1].point
        else:
        	p=list1[dele-1].point
        	p.next=list1[dele+1].point
        	return head
s=p=ListNode(1)
for i in range(2,6):
	q=ListNode(i)
	p.next=q
	p=q
n=2
t=Solution()
print (t.removeNthFromEnd(s,n))  
while s!=None:
	print(s.val)
	s=s.next