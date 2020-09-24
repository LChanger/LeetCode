class Solution:
    def search(self, nums, target):
        '''
        整体思路：先找到截断旋转的位置，然后使用二分查找，实际的mid位置需要考虑截断的位置
        '''
        n=len(nums)
        low=0
        high=n-1
        while low<high:
            mid=(low+high)//2#此处mid取低位，防止陷入死循环
            if nums[mid]>nums[high]:low=mid+1
            else:high=mid#为了保证high为最小值，此处不能使high=mid-1
        #设截断位置为truncate ,则此时truncate=low=high
        truncate=low
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            truemid=(mid+truncate)%n # 真实的mid位置为 ((truncate+low+truncate+high)//2)%n=(mid+truncate)%n
            if nums[truemid]==target:return truemid+1
            elif nums[truemid]<target:low=mid+1
            else:high=mid-1
        return -1
nums=[5,7,12,15,1,3]
target = 1
s=Solution()
print(s.search(nums,target))