class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums)==0:return 0
        # start=end=0#两个指针
        Max=cur=nums[0]#max start和end之间的数之和， cur 当前指针前进到的位置的最大值
        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            if cur>=Max:
                # end=i
                Max=cur
        return Max
n=[-2,1,-3,4,-1,2,1,-5,4]
t=Solution()
print (t.maxSubArray(n))