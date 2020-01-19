class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda i: i[0])
        res=[]
        for i in intervals:
            if res and res[-1][1]>=i[0]:
                res[-1][1]=max(res[-1][1],i[1])
            else:
                res.append(i)
        return res
# n=[[1,4],[0,2],[3,5]]
# t=Solution()
# print (t.insert(n))