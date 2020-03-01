# -*- coding:utf-8 -*-
class Heap():
    def __init__(self):
        self.heap=[]
    def MAX_Heapify(self,heap,root,size):
        while 2*root+1<size:
            child=2*root+1#左子节点
            #TODO 重点！！！必须关注child+1与size的大小
            if child+1<size and heap[child]<heap[child+1]:child+=1
            if heap[root]<heap[child]:
                heap[root],heap[child]=heap[child],heap[root]
                root,child=child,root
            else:break
    def Build_MAX_Heap(self,heap):
        self.heap=heap
        #从最后一个叶子结点的父节点开始
        for i in range((len(self.heap)-2)//2,-1,-1):
            self.MAX_Heapify(self.heap,i,len(self.heap))
    def sift_up(self,heap,size):
        child=size-1
        parent=(child-1)//2
        while parent>=0 and heap[parent]<heap[child]:
            heap[parent],heap[child]=heap[child],heap[parent]
            parent,child=(parent-1)//2,parent
    def add_Node(self,val):
        self.heap.append(val)
        self.sift_up(self.heap,len(self.heap))
    def get_MAX(self):
        if not self.heap:return None
        self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
        self.MAX_Heapify(self.heap,0,len(self.heap)-1)
        return self.heap.pop()
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num:return []
        j=size-1
        que=Heap()
        que.Build_MAX_Heap(num[:min(len(num),j+1)])
        res=[]
        if j>len(num)-1:res.append(que.get_MAX())
        while j<len(num)-1:
            res.append(que.get_MAX())
            j+=1
            que.add_Node(num[j])
        res.append(que.get_MAX())
        return res
s=Solution()
t=[2,3,4,2,6,2,5,1]
print(s.maxInWindows(t,3))