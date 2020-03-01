# 先将array1移动到后半部分，然后进行归并排序
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=m-1
        for i in range(len(nums1)-1,len(nums1)-1-m,-1):
            nums1[i]=nums1[j]
            j-=1
        i=len(nums1)-m
        j=0
        k=0
        while i<len(nums1) and j<n:
            if nums1[i]<nums2[j]:
                nums1[k]=nums1[i]
                k+=1
                i+=1
            else:
                nums1[k]=nums2[j]
                k+=1
                j+=1
        if j==n:
            while i<len(nums1):
                nums1[k]=nums1[i]
                k+=1
                i+=1
        else:
            while j<n:
                nums1[k]=nums2[j]
                k+=1
                j+=1
        
nums1=[1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]      
n= 3
t = Solution()
t.merge(nums1,m,nums2,n)
print(nums1)
