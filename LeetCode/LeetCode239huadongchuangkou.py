class Solution:
    def maxSlidingWindow(self, nums,k: int):
        if k==1:return nums
        if k*len(nums)==0:return []
        if len(nums)<=k:return [max(nums)]
        from collections import deque
        que=deque()
        def clean(i):
            if que and i-k==que[0]:
                que.popleft()
            while que and nums[i]>nums[que[-1]]:
                que.pop()
        for i in range(k):
            clean(i)
            que.append(i)
        output=[nums[que[0]]]
        for i in range(k,len(nums)):
            clean(i)
            que.append(i)
            # print(f'{i}:{que}')
            output.append(nums[que[0]])
        return output
#官方题解
import collections
class Solution0:
    def maxSlidingWindow(self, nums, k: int) :
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans

nums=[1,2,3,-1,-2,-3,-4]
k=3
print(Solution().maxSlidingWindow(nums,k))