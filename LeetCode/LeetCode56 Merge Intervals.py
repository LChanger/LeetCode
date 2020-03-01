class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda i: i[0])
        res=[]
        for i in intervals:
            if res and i[0]<=res[-1][1]:
                res[-1][1]=max(i[1],res[-1][-1])
            else:res.append(i)
        return res
    # -----------------------------------method one -----------------------------------
    # def merge(self, intervals):
    #     def takeSecond(elem):
    #         return elem[0]
    #     intervals.sort(key=takeSecond)
    #     for j in range(len(intervals)-1,-1,-1):
    #         for i in range(j-1,-1,-1):
    #             if intervals[i][1]>=intervals[j][0]:
    #                 intervals[i][1]=intervals[j][1] if intervals[i][1]<intervals[j][1] else intervals[i][1]
    #                 intervals[i][0]=intervals[j][0] if intervals[i][0]>intervals[j][0] else intervals[i][0]
    #                 del intervals[j]
    #                 break
    #     return intervals
n=[[1,4],[0,2],[3,5]]
t=Solution()
print (t.merge(n))