class MaxHeap:
    def __init__(self):
        self.tree=[]#三元组
    def sit_down(self,start,end):
        child=start*2+1
        while child<=end:
            if child+1<=end and self.tree[child][0]<self.tree[child+1][0]:
                child+=1
            if self.tree[child][0]>self.tree[start][0]:
                self.tree[child],self.tree[start]=self.tree[start],self.tree[child]
                start=child
                child=start*2+1
            else:
                break
    

class Solution:
    def kClosest(self, points, K: int):
        import math
        def count_distance(x,y):
            return math.sqrt(x*x+y*y)
        if len(points)<=K:return points
        mh=MaxHeap()
        for i in range(K):
            mh.tree.append((count_distance(points[i][0],points[i][1]),points[i][0],points[i][1]))
        end=K-1
        start=(end-1)//2
        for i in range(start,-1,-1):
            mh.sit_down(i,end)
        for i in range(K,len(points)):
            distance=count_distance(points[i][0],points[i][1])
            if distance<mh.tree[0][0]:
                mh.tree[0]=(distance,points[i][0],points[i][1])
                mh.sit_down(0,end)
        res=[]
        for d,x,y in mh.tree:
            res.append([x,y])
        return res
points=[[3,3],[5,-1],[-2,4]]
K=2
print(Solution().kClosest(points,K))