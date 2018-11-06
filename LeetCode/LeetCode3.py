# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         l1=len(nums1)
#         l2=len(nums2)
#         if l1%2!=0 and l2%2!=0:
#         	i=l1/2
#         	j=l2/2
#         	if nums1[i]==nums2[j]:
#         		return nums1[i]
#         	elif nums1[i]>nums2[j]:
#         		nums3=nums1[:i]+nums2[j:]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2
#         	else:
#         		nums3=nums1[i:]+nums2[:j]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2
#         elif l1%2==0 and l2%2==0:
#         	i=l1/2-1
#         	j=l2/2-1
#         	if nums1[i]==nums2[j]:
#         		if nums1[i+1]>nums2[j+1]:
#         			return (nums1[i]+nums2[j+1])/2
#         		return (nums1[i+1]+nums2[j])/2
#         	elif nums1[i]>nums2[j]:
#         		nums3=nums1[:i]+nums2[j+1:]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2
#         	else:
#         		nums3=nums1[i+1:]+nums2[:j]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2
#         elif l1%2==0:
#         	i=l1/2-1
#         	j=l2/2
#         	if nums1[i]==nums2[j]:
#         		return nums1[i]
#         	elif nums1[i]>nums2[j]:
#         		nums3=nums1[:i]+nums2[j:]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2
#         	else:
#         		nums3=nums1[i+1:]+nums2[:j]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2
#         else:
#         	i=l1/2
#         	j=l2/2-1
#         	if nums1[i]==nums2[j]:
#         		return nums1[i]
#         	elif nums1[i]>nums2[j]:
#         		nums3=nums1[:i]+nums2[j+1:]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2
#         	else:
#         		nums3=nums1[i:]+nums2[:j]
#         		nums3.sort()
#         		return (nums3[len(nums3)//2] + nums3[~len(nums3)//2]) / 2


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1,l2=len(nums1),len(nums2)
        if l1>l2:
        	nums1,nums2,l1,l2=nums2,nums1,l2,l1
        imin,imax=0,l1
        k=(l1+l2+1)/2
        while(1):
        	i=(imin+imax)/2
        	j=k-i
        	if i<l1 and nums1[i]<nums2[j-1]:
        		imin+=1
        	elif i>0 and nums1[i-1]>nums2[j]:
        		imax-=1
        	else:
        		if i==0:a=nums2[j-1]
        		elif j==0:a=nums1[i-1]
        		else:a=max(nums1[i-1],nums2[j-1])
        		if (l1+l2)%2==1:return a
        		if i==l1:b=nums2[j]
        		elif j==l2:b=nums1[i]
        		else:b=min(nums1[i],nums2[j])
        		return (float)(a+b)/2
nums1=[1,1]
nums2=[1,2]
t=Solution()
print (t.findMedianSortedArrays(nums1,nums2))


