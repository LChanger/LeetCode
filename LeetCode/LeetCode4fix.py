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


class Solution1(object):
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

#中位数是 求 第(m+n+1)//2和(m+n+2)//2的均值
#递归，寻找第k大小的数
import sys
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def binarySearch(start1,end1,start2,end2,k):
            if end1<start1:return nums2[start2+k-1]
            if end2<start2:return nums1[start1+k-1]
            if k==1:return min(nums1[start1],nums2[start2])
            find1=k//2+start1-1
            find2=k-k//2+start2-1
            #如果一个数组超出了k//2的范围，那么一定是抛弃另一个数组前K//2的部分
            mid1=nums1[find1] if find1<=end1 else sys.maxsize
            mid2=nums2[find2] if find2<=end2 else sys.maxsize
            if mid1==mid2:
                return nums1[find1]
            if mid1<mid2:
                #第k大的数一定不在nums1[start1:find1+1],抛弃之
                return binarySearch(find1+1,end1,start2,end2,k-k//2)
            else:
                return binarySearch(find1,end1,find2+1,end2,k//2)

        l=(len(nums1)+len(nums2)+1)//2
        r=(len(nums1)+len(nums2)+2)//2
        return (binarySearch(0,len(nums1)-1,0,len(nums2)-1,l)+binarySearch(0,len(nums1)-1,0,len(nums2)-1,r))/2

nums1=[1]
nums2=[2,3,4,5,6]
t=Solution()
print (t.findMedianSortedArrays(nums1,nums2))


