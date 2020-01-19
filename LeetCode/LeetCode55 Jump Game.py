class Solution:
    def canJump(self, nums) -> bool:
        i=0
        next_step=nums[0]
        while i<=next_step:
            if nums[i]+i>next_step:next_step=nums[i]+i
            if next_step>=len(nums):return True
            i+=1
        if next_step<len(nums)-1:return False  
        return True      
        # while i<len(nums):
        #     next_step=nums[i]
        #     cur_far=nums[0]
        #     while i<=cur_far:
        #         if nums[i]+i>next_step:next_step=nums[i]+i
        #         if next_step>=len(nums):return True
n=[3,2,1,0,4]
t=Solution()
print (t.canJump(n))