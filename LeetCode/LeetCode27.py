# Definition for singly-linked list.
nums = [3,2,2,3]

# 思路，纸面上画一下每步的步骤
class Solution:
    def removeElement(self, nums,val: int) -> int:
        if len(nums)==0:return 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:nums.pop(i)
        return len(nums)

t = Solution()
t.removeElement(nums,3)
