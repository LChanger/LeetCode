class Solution:
    def searchRange(self, nums, target: int):
        if not nums:return [-1,-1]
        self.direct=-1#向前找
        self.start=-1
        self.end=-1
        def pre_binary_search(start,end):
            if start>end:return -1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    if mid-1>=0 and nums[mid-1]==nums[mid]:
                        return pre_binary_search(start,mid-1)
                    return mid
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return -1
        def back_binary_search(start,end):
            if start>end:return -1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    if mid+1<len(nums) and nums[mid+1]==nums[mid]:
                        return back_binary_search(mid+1,end)
                    return mid
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return -1
        start=0
        end=len(nums)-1
        axis=-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                axis=mid
                break
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        if axis==-1:return [-1,-1]
        self.start=pre_binary_search(0,axis)
        self.end=back_binary_search(axis,len(nums)-1)
        return [self.start,self.end]
nums=[5,7,7,8,8,10]
target=8
print(Solution().searchRange(nums,target))