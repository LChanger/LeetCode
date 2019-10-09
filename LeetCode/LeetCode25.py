# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l3.next = l4
l4.next=l5
l2.next = l3


# 思路，纸面上画一下每步的步骤
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 记录链表长度
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        stop = n - n % k  # 要停止的结点
        # fir为每个group的首结点,last为每个group的末结点，p，q为前进的两个指针，每次交换p，q, setp为目前p所处的位置，结点从1开始计数
        if not head: return head
        fir = res = last=ListNode(None)  # 定义一个首结点置空
        res.next = head
        step = 0#为要处理的一下个结点
        while step < stop and fir.next:
            i = 1
            fir = fir.next
            p=fir
            step+=1
            q=p.next
            while i < k and q:
                fir.next=q.next
                q.next=p
                p=q
                q=fir.next
                i+=1
                step+=1
            #此时p位于某一组的最后一个结点，q为下一组的第一个结点,fir指向q
            last.next=p
            last=fir
        return res.next

t = Solution()
t.reverseKGroup(l1,2)
