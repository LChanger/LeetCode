class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result=[]
        if len(candidates)==0 or candidates[0] > target:return result
        def recursionSum(low,target,temp):
            if target==0 and temp not in result:
                result.append(temp)
                return
            elif low>=len(candidates) or target<candidates[low]:
                return
            high=self.search(candidates,target)
            i=low+1
            while i<=high+1:
                recursionSum(i,target-candidates[i-1],temp+[candidates[i-1]])
                i+=1
        recursionSum(0,target,[])
        return result

    def search(self, candidates, target: int):
        low=0
        high=len(candidates)-1
        while low<high:
            mid=int((low+high)/2)
            if candidates[mid]==target and candidates[mid] not in candidates[mid:mid+1]:return mid
            elif candidates[mid]<=target:low=mid+1
            else:high=mid
        return high



c=[2,5,2,1,2]
x=5
t=Solution()
print (t.combinationSum2(c,x))
