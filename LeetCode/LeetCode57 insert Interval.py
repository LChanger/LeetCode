# class Solution:
#     def insert(self, intervals, newInterval):
#         intervals.append(newInterval)
#         intervals.sort(key=lambda i: i[0])
#         res=[]
#         for i in intervals:
#             if res and res[-1][1]>=i[0]:
#                 res[-1][1]=max(res[-1][1],i[1])
#             else:
#                 res.append(i)
#         return res


class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:return [newInterval]
        res=[]
        is_add=False
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            #两种情况
            #已经插入
            if is_add:
                if start>res[-1][1]:
                    res.append(intervals[i])
                elif end>res[-1][1]:
                    res[-1][1]=end
                    
            #没有插入,两个区间相交或不相交，若相交有四种关系
            else:
                if end<newInterval[0]:
                    res.append(intervals[i])
                    continue
                elif start>newInterval[1]:
                    res.append(newInterval)
                    res.append(intervals[i])
                elif newInterval[0]>=start and newInterval[1]<=end:
                    res.append(intervals[i])
                elif start>=newInterval[0] and end>=newInterval[1]:
                    res.append([newInterval[0],end])
                elif start>=newInterval[0] and end<=newInterval[1]:
                    res.append(newInterval)
                elif start<=newInterval[0] and end<=newInterval[1]:
                    res.append([start,newInterval[1]])
                is_add=True
        return res

n=[[1,2],[3,5],[6,7],[8,10],[12,16]]
x=[4,8]
t=Solution()
print (t.insert(n,x))