#思路：二分法
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        #求小于等于mid的所有个数
        def count(mid):
            x=len(matrix)-1
            y=0
            cnt=0
            while x>=0 and y<len(matrix[0]):
                if matrix[x][y]<=mid:y+=1
                else:
                    cnt+=y
                    x-=1
            if y==len(matrix[0]):cnt+=y*(x+1)
            return cnt
        l=matrix[0][0]
        r=matrix[-1][-1]
        while l<r:
            mid=(l+r)//2
            if count(mid)>=k:
                r=mid
            else:
                l=mid+1
        return r
nums=[[1,5,9],[10,11,13],[12,13,15]]
k=8
print(Solution().kthSmallest(nums,k))