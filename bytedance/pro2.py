n=int(input())
nums=list(map(lambda x: int(x),input().split()))
def gettimes(nums):
    res=0
    # from collections import deque()
    for i in range(len(nums)-2,-1,-1):
        if nums[i+1]>=nums[i]:continue
        times=(nums[i]-1)//nums[i+1]
        res+=times
        nums[i]=nums[i]//(times+1)
    return res
print(gettimes(nums))