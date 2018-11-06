class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=0
        x=y=z=0
        s=nums[0]+nums[1]+nums[2]
        ss=target-s
        for i in range(len(nums)):
        	if i>0 and nums[i-1]==nums[i]:continue
        	l,h=i+1,len(nums)-1
        	while l<h:
        		if abs(target-nums[i]-nums[l]-nums[h])<ss:
        			ss=abs(target-nums[i]-nums[l]-nums[h])
        			s=nums[i]+nums[l]+nums[h]
        		if nums[i]+nums[l]+nums[h]<target:l+=1
        		elif nums[i]+nums[l]+nums[h]>target:h-=1
        		else:return s
        		pass
        return s
t=Solution()
nums=[-1,2,1,-4]
target=1
print(t.threeSumClosest(nums,target))