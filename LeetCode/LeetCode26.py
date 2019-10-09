# Definition for singly-linked list.
nums = [1,1,2]

# 思路，纸面上画一下每步的步骤
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)==0:return 0
        for i in range(len(nums)-1,0,-1):
            if nums[i]==nums[i-1]:nums.pop(i)
        return len(nums)

t = Solution()
t.removeDuplicates(nums)
