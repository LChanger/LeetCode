# 记录两个轴，若当前轴间距小于最优间距则更新
class Solution:
    def subsets(self, nums):
        res=[]
        def curSubset(temp,count,index):#temp是当前生成的subset，count是要生成的subset元素长度，index是当前要扫位置起点
            if count==0:
                res.append(temp)
                return
            for i in range(index,len(nums)-count+1):
                curSubset(temp+[nums[i]],count-1,i+1)
        for i in range(len(nums)+1):
            curSubset([],i,0)
        return res
nums = [1,2,3]
t = Solution()
print(t.subsets(nums))
