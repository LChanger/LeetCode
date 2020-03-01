# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:return 0
        def merge(left,right):
            l,r=0,0
            res=[]
            count=0
            while l<len(left) and r<len(right):
                if left[l]>right[r]:
                    res.append(right[r])
                    count+=(len(left)-l)
                    r+=1 
                else:
                    res.append(left[l])
                    l+=1
            for i in range(l,len(left)):
                res.append(left[i])
            for i in range(r,len(right)):
                res.append(right[i])
            return count,res
        def mergesort(data):
            if len(data)<=1:return 0,data
            length=len(data)//2
            lc,left=mergesort(data[:length])
            rc,right=mergesort(data[length:])
            count,res=merge(left,right)
            return lc+rc+count,res
        count,_=mergesort(data)
        return count

nums=[1,2,3,4,5,6,7,0]
s=Solution()
print(s.InversePairs(nums))