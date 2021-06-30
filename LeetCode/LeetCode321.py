class Solution:
    def maxNumber(self, nums1, nums2, k: int):
        def get_Max_num(nums,k):
            if k==0:return []
            stack=[]
            to_rm=len(nums)-k
            for digit in nums:
                while to_rm>0 and stack and stack[-1]<digit:
                    stack.pop()
                    to_rm-=1
                stack.append(digit)
            return stack[0:k]
        def merge(nums1,nums2):
            res=[]
            start1=0
            start2=0
            while start1<len(nums1) and start2<len(nums2):
                if nums1[start1:]>nums2[start2:]:
                    res.append(nums1[start1])
                    start1+=1
                else:
                    res.append(nums2[start2])
                    start2+=1
            res+=nums1[start1:]
            res+=nums2[start2:]
            return res
        return max(merge(get_Max_num(nums1, i), get_Max_num(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))


nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
print(Solution().maxNumber(nums1,nums2,k))