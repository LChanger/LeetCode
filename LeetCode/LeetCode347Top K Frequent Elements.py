class Solution:
    def topKFrequent(self, nums, k: int) :
        from collections import defaultdict
        mapn=defaultdict(int)
        for i in range(len(nums)):
            mapn[nums[i]]+=1
        temp=[]
        for key in mapn:
            temp.append((key,mapn[key]))
        temp.sort(key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(temp[i][0])
        return res
nums = [1,1,1,2,2,3]
k = 2
s=Solution()
print(s.topKFrequent(nums,k))