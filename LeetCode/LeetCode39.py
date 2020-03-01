class Solution:
    #记住 1放在第0个位置，2放在第一个位置，以此类推
    def firstMissingPositive(self, nums) -> int:
        i=0
        n=len(nums)
        while i<len(nums):
            while 0<nums[i]<=n and nums[i]!=i+1 and nums[nums[i] - 1]!=nums[i]:
                 # 交换位置  数比位置大1
                nums[nums[i] - 1], nums[i] = nums[i],nums[nums[i] - 1]
            i+=1
        i=0
        while i<len(nums) and nums[i]==i+1:i+=1
        return i+1

c=[1,1]

t=Solution()
print (t.firstMissingPositive(c))
