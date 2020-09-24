# 记录两个轴，若当前轴间距小于最优间距则更新
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        left=0
        sum=0
        res=len(nums)+1 #设置一个不可能的最大值，用于初次比较
        for i in range(len(nums)):
            sum+=nums[i]
            while left<len(nums) and sum-nums[left]>=s:
                sum-=nums[left]#总和减去左轴
                left+=1#左轴右移
            if sum>=s and i-left+1<res:
                res=i-left+1
        return res if res<=len(nums) else 0
s = 7
nums = [2,3,1,2,4,3]
t = Solution()
print(t.minSubArrayLen(s,nums))
