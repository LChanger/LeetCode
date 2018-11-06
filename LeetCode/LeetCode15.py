class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
        	if i>0 and nums[i-1]==nums[i]:continue
        	l,h=i+1,len(nums)-1
        	while l<h:
        		snum=nums[i]+nums[l]+nums[h]
        		if snum<0:l+=1
        		elif snum>0:h-=1
        		else:
        			res.append((nums[i],nums[l],nums[h]))
        			while l<h and nums[l]==nums[l+1]:l+=1
        			while l<h and nums[h]==nums[h-1]:h-=1
        			l+=1
        			h-=1
        		pass
        return res
