#思路：先找到旋转的点，然后按二分法查找
class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:return -1
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[high]:low=mid+1
            else:high=mid
        truncate=low
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            midTrue=(truncate+mid)%len(nums)
            if nums[midTrue]==target:return midTrue
            elif nums[midTrue]<target:low=mid+1
            else:high=mid-1
        return -1
nums=[4,5,6,7,0,1,2]
target=1
s=Solution()
print(s.search(nums,target))