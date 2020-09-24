# T=int(input())
# def find(beigin,end,nums):
#     le=1
#     preB=nums[beigin]
#     preE=nums[end]
#     posB=beigin-1
#     posE=end+1
#     from collections import deque
#     stack1=deque()
#     stack2=deque()
#     stack1.append(nums[beigin])
#     while beigin>=0:
#         if nums[beigin]>nums[stack1[-1]]:
#             stack1.append()
#     while True:
#         while posB>=0 and nums[posB]<preB:posB-=1
#         while posE<len(nums) and nums[posE]>preE:posE+=1
#         if posB>=0 and posE<len(nums):
#             preB=nums[posB]
#             preE=nums[posE]
#             le+=1
#         else:
#             break
#     return le*2
# def slove(nums):
#     max_val=0
#     cache={}
#     for i in range(len(nums)):
#         if nums[i] in cache:
#             max_val=max(max_val,find(cache[nums[i]],i,nums))
#         cache[nums[i]]=i
#     return max_val
    
# for i in range(T):
#     n=int(input())
#     nums=list(map(int,input().split()))
#     print(slove(nums))



T=int(input())
def find(beigin,end,nums):
    le=1
    preB=nums[beigin]
    preE=nums[end]
    posB=beigin-1
    posE=end+1
    from collections import deque
    stack1=deque()
    stack2=deque()
    stack1.append(nums[beigin])
    while beigin>=0:
        if nums[beigin]>nums[stack1[-1]]:
            stack1.append()
    while True:
        while posB>=0 and nums[posB]<preB:posB-=1
        while posE<len(nums) and nums[posE]>preE:posE+=1
        if posB>=0 and posE<len(nums):
            preB=nums[posB]
            preE=nums[posE]
            le+=1
        else:
            break
    return le*2
def slove(nums):
    max_val=0
    cache={}
    leftdp=[1]*len(nums)
    rightdp=[1]*len(nums)
    
    for i in range(1,len(leftdp)):
        for j in range(i-1,-1,-1):
            if nums[j]>nums[i]:
                leftdp[i]=max(leftdp[i],leftdp[j]+1)
    
    for i in range(len(rightdp)-2,-1,-1):
        for j in range(i+1,len(rightdp)):
            if nums[j]>nums[i]:
                rightdp[i]=max(rightdp[i],rightdp[j]+1)
    
    for i in range(len(nums)):
        if nums[i] in cache:
            left=leftdp[cache[nums[i]]]
            right=rightdp[i]
            max_val=max(max_val,min(left,right))
        cache[nums[i]]=i
    return max_val*2
    
for i in range(T):
    n=int(input())
    nums=list(map(int,input().split()))
    print(slove(nums))