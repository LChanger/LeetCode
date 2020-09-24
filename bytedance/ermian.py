def find_min_subarray(nums):
    if not nums:return 0
    cur=0
    min_val=nums[0]
    for i in range(len(nums)):
        cur=min(cur+nums[i],nums[i])
        min_val=min(min_val,cur)
    return min_val
nums=[1,4,-5,3,-6,2,-2,3,-5]
print(find_min_subarray(nums))