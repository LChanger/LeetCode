# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(5)
l2 = ListNode(7)
l1.next = l2
l3 = ListNode(1)
l4 = ListNode(8)
l3.next = l4
l2.next = l3

# 思路，纸面上画一下每步的步骤
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # k,p,q为三个依次相连的节点，每次交换p,q两结点，然后前进两步，若p或q为空则停止前进，返回res.next
        res = k = ListNode(None)  # 定义一个首结点置空
        k.next=head
        p = k.next
        while p:
            if not p.next: break
            q = p.next
            k.next = q
            p.next = q.next
            q.next = p
            k = p
            p = k.next
        return res.next
t = Solution()
t.swapPairs(l1)
