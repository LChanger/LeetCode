def reSum(nums):
    sum=0
    for  i in range(len(nums)):
        sum+=nums[i]
    nums.sort(reverse=True)
    if sum%2==1:return False
    target=sum//2
    left=0
    def recur(sum,start):
        if sum==target:return True
        if sum>target:return False
        for i in range(start,len(nums)):
            if recur(sum+nums[i],i+1):return True
        return False
    return recur(0,0)
nums=[1,2,2,10,5]
print(reSum(nums))