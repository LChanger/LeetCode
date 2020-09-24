#思路：先按照左边界排序，然后遍历列表，保存一个队列，每次判断队列中元素的高度决定是否要加入结果中，当前元素左端点之左的节点则pop
class Solution:
    def getSkyline(self,buildings):
        res=[]
        #寻找大于target的数的位置
        def binary_search(heights,target):
            low=0
            high=len(heights)-1
            while low<high:
                mid=(low+high)//2
                if heights[mid]==target:return mid
                elif heights[mid]<target:
                    low=mid+1
                else:
                    high=mid
            return low
        all_line=[]
        for b in buildings:
            all_line.append((b[0],-b[2]))
            all_line.append((b[1],b[2]))
        from functools import cmp_to_key
        def cmpe(a,b):
            if a[0]!=b[0]:
                return a[0]-b[0]
            return a[1]-b[1]
        all_line.sort(key=cmp_to_key(cmpe))
        heights=[0]
        last=[0,0]
        for line in all_line:
            if line[1]<0:
                if -line[1]>heights[-1]:heights.append(-line[1])
                else:
                    index=binary_search(heights,-line[1])
                    heights.insert(index,-line[1])
            else:
                index=binary_search(heights,line[1])
                heights.pop(index)
            if heights[-1]!=last[1]:
                res.append([line[0],heights[-1]])
                last=[line[0],heights[-1]]
        return res
buildings=[[0,2,3],[2,5,3]]
print(Solution().getSkyline(buildings))