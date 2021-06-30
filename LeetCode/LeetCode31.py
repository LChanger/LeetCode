# # Definition for singly-linked list.
# s ="aaa"
# words = ["aa","aa"]

# # 思路，纸面上画一下每步的步骤
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         intMax, intMin = 2147483647, -2147483648
#         isnegative=(dividend<0)^(divisor<0)
#         dividend,divisor=abs(dividend),abs(divisor)
#         res=0
#         while dividend>=divisor:
#             tmp,val=divisor,1
#             while dividend>=tmp:
#                 res+=val
#                 dividend-=tmp
#                 tmp<<=1
#                 val<<=1
#         if isnegative:
#             res=-res
#             return max(res,intMin)
#         return min(res,intMax)

# #参考思路 https://www.cnblogs.com/grandyang/p/4521224.html
# t = Solution()
# print(t.divide(-7,3))


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:return []
        to_exchange=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                to_exchange=i
                break
        if to_exchange==-1:return nums[::-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>nums[to_exchange]:
                nums[i],nums[to_exchange]=nums[to_exchange],nums[i]
                break
        nums[to_exchange+1:len(nums)]=nums[len(nums)-1:to_exchange:-1]
        return nums
nums=[3,2,1]
print(Solution().nextPermutation(nums))