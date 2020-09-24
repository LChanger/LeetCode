# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
l1=ListNode(5)
l2=ListNode(7)
l1.next=l2
l3=ListNode(1)
l4=ListNode(8)
l3.next=l4
x=[]
x.append(l1)
x.append(l3)
#思路，应用优先级队列
class Solution0:
	def mergeKLists(self, lists):
		"""
        :type lists: List[ListNode]
        :rtype: ListNode
        """
		import queue
		que=queue.PriorityQueue()
		for i,node in enumerate(lists):
			if node:que.put((node.val,i,node))#将每个非空链表首结点放入优先级队列
		head=step=ListNode(None)#step为待输出链表的当前末尾结点
		while not que.empty():
			_,idx,step.next=que.get()#队列首元素出队，作为待输出链表的下一结点
			step=step.next#step后移
			if step.next!=None:que.put((step.next.val,idx,step.next))#待输出链表的当前末尾结点的下一结点若不为空则入队
		return head.next
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        from queue import PriorityQueue
        if not lists:return None
        pq=PriorityQueue()
        for i in range(len(lists)):
            if lists[i]:pq.put((lists[i].val,lists[i]))
        head=ListNode(0)
        p=head
        while not pq.empty():
            val,p.next=pq.get()
            p=p.next
            if p.next:pq.put((p.next.val,p.next))
        return head.next
s=Solution()
print(s.mergeKLists(x))