class Solution:
    def combinationSum(self, candidates, target):
        result=[]
        candidates.sort()
        if len(candidates)==0 or candidates[0] > target:return result
        def recursionSum(low,target,temp):
            if target<0:
                return
            if target==0:
                result.append(temp)
                return
            index=self.search(candidates,target)
            i=low
            while i<index+1:
                recursionSum(i,target-candidates[i],temp+[candidates[i]])
                i+=1

        recursionSum(0,target,[])
        return result

    def search(self, candidates, target: int):
        low=0
        high=len(candidates)-1
        while low<high:
            mid=int((low+high)/2)
            if candidates[mid]==target:return mid
            elif candidates[mid]<target:low=mid+1
            else:high=mid-1
        return high



c=[2,3,6,7]
x=7
t=Solution()
print (t.combinationSum(c,x))
