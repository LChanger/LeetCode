class MedianFinder:
    #思路，维护一个最大堆和一个最小堆，保证两者数量最大差1
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap=[]
        self.min_heap=[]

    def max_heap_sit_up(self,num):
        self.max_heap.append(num)
        index=len(self.max_heap)-1
        while index>0:
            parent=(index-1)//2
            if self.max_heap[index]<=self.max_heap[parent]:
                break
            self.max_heap[index],self.max_heap[parent]=self.max_heap[parent],self.max_heap[index]
            index=parent
    def max_heap_pop(self):
        self.max_heap[0],self.max_heap[-1]=self.max_heap[-1],self.max_heap[0]
        res=self.max_heap[-1]
        self.max_heap.pop()
        cur=0
        while 2*cur+1<len(self.max_heap):
            child=cur*2+1
            if child+1<len(self.max_heap) and self.max_heap[child+1]>self.max_heap[child]:
                child+=1
            if self.max_heap[cur]>=self.max_heap[child]:break
            self.max_heap[cur],self.max_heap[child]=self.max_heap[child],self.max_heap[cur]
            cur=child
        return res

    def min_heap_pop(self):
        self.min_heap[0],self.min_heap[-1]=self.min_heap[-1],self.min_heap[0]
        res=self.min_heap[-1]
        self.min_heap.pop()
        cur=0
        while 2*cur+1<len(self.min_heap):
            child=cur*2+1
            if child+1<len(self.min_heap) and self.min_heap[child+1]<self.min_heap[child]:
                child+=1
            if self.min_heap[cur]<=self.min_heap[child]:break
            self.min_heap[cur],self.min_heap[child]=self.min_heap[child],self.min_heap[cur]
            cur=child
        return res

    def min_heap_sit_up(self,num):
        self.min_heap.append(num)
        index=len(self.min_heap)-1
        while index>0:
            parent=(index-1)//2
            if self.min_heap[index]>=self.min_heap[parent]:
                break
            self.min_heap[index],self.min_heap[parent]=self.min_heap[parent],self.min_heap[index]
            index=parent

    def addNum(self, num: int) -> None:
        self.max_heap_sit_up(num)
        if len(self.max_heap)-len(self.min_heap)>=2:
            res=self.max_heap_pop()
            self.min_heap_sit_up(res)
        #如果左边大于右边了，交换一下
        if self.min_heap and self.min_heap[0]<self.max_heap[0]:
            min_val=self.min_heap_pop()
            max_val=self.max_heap_pop()
            self.min_heap_sit_up(max_val)
            self.max_heap_sit_up(min_val)

    def findMedian(self) -> float:
        if len(self.max_heap)==len(self.min_heap):
            return (self.max_heap[0]+self.min_heap[0])/2
        return self.max_heap[0]
actions=["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
vals=[[],[1],[],[2],[],[3],[],[4],[],[5],[],[6],[],[7],[],[8],[],[9],[],[10],[]]

M=MedianFinder()
for i in range(1,len(actions)):
    if actions[i]=="addNum":
        val=vals[i][0]
        M.addNum(val)
        print("[]\t")
    elif actions[i]=="findMedian":
        print(f"{M.findMedian()}\t")