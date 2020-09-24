class Solution:
    def kthSmallestPrimeFraction(self, A, K: int):
        #寻找小于等于mid的元素个数
        def find_m(mid):
            slow=0
            fast=1
            cnt=0
            p=A[0]
            q=A[-1]
            while fast<len(A):
                if A[fast]*mid>=A[slow]:
                    if p*A[fast]<q*A[slow]:
                        p=A[slow]
                        q=A[fast]
                    cnt+=len(A)-fast
                    slow+=1
                else:
                    fast+=1
            return cnt,p,q
        l=0
        r=1
        while l<r:
            mid=(l+r)/2
            cnt,p,q=find_m(mid)
            if cnt==K:return [p,q]
            elif cnt<K:l=mid
            else:r=mid
        return [] 
A =[1,2,3,5]
K = 3
print(Solution().kthSmallestPrimeFraction(A,K))