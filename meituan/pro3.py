
class Solution1:
    def subsets(self, nums):
        self.res=0
        def curSubset(temp,count,index):#temp是当前生成的subset，count是要生成的subset元素长度，index是当前要扫位置起点
            if count==0:
                # res.append(temp)
                return
            for i in range(index,len(nums)-count+1):
                if nums[i]%(temp+1)==0:
                    self.res=self.res%998244353+1
                    curSubset(temp+1,count-1,i+1)
        for i in range(1,len(nums)+1):
            curSubset(0,i,0)
        return self.res

class Solution3:
    def subsets(self, nums):
        res=[]
        def curSubset(temp,count,index):#temp是当前生成的subset，count是要生成的subset元素长度，index是当前要扫位置起点
            if count==0:
                res.append(temp)
                return
            for i in range(index,len(nums)-count+1):
                if nums[i]%(len(temp)+1)==0:
                    curSubset(temp+[nums[i]],count-1,i+1)
        for i in range(1,len(nums)+1):
            curSubset([],i,0)
        return res

class Solution2:
    def subsets(self, nums):
        res=[]
        self.num=0
        def curSubset(temp,count,index):#temp是当前生成的subset，count是要生成的subset元素长度，index是当前要扫位置起点
            if count==0:
                self.num+=1
                res.append(temp)
                return
            for i in range(index,len(nums)-count+1):
                if nums[i]%(temp+1)==0:
                    curSubset(temp+1,count-1,i+1)
        for i in range(1,len(nums)+1):
            curSubset(0,i,0)
        return self.num
        
class Solution:
    def subsets(self, nums):
        self.res=0
        def curSubset(temp,count,index):#temp是当前生成的subset，count是要生成的subset元素长度，index是当前要扫位置起点
            if count==0:
                self.res=self.res%998244353+1
                # res.append(temp)
                return
            for i in range(index,len(nums)-count+1):
                if nums[i]%(temp+1)==0:
                    curSubset(temp+1,count-1,i+1)
        for i in range(1,len(nums)+1):
            curSubset(0,i,0)
        return self.res


class Solution7:
    def subsets(self, nums):
        allSubsets = []
        def subsetFinder(nums, currentSubset,count):
            if len(nums) == 0:
                self.res+=1
                allSubsets.append(currentSubset)
                return
            if nums[0]%(count)==0:subsetFinder(nums[1:], list(currentSubset),count)
            if nums[0]%(count+1)==0:subsetFinder(nums[1:], list(currentSubset + [nums[0]]),count+1)
        
        subsetFinder(nums, [],0)
        return allSubsets

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort the list so duplicates are close to each other
        nums.sort()
        startIndex, endIndex = 0, 0
        subsets = []
        subsets.append([])
        self.res=0
        for i in range(len(nums)):
            if i==0:
                startIndex=0 #要添加新元素的子集的起始位置
            startIndex=1
            if i>0 and nums[i-1]==nums[i]:startIndex=endIndex+1
            endIndex=len(subsets)-1 #要添加新元素的子集的终点位置
            for j in range(startIndex,endIndex+1):
                newset=subsets[j][:]
                if nums[i]%(len(newset)+1)==0:
                    newset.append(nums[i])
                    subsets.append(newset)
                    self.res=self.res%998244353+1
        return subsets

a=input()
b=input()
b=b.split()
a=int(a)
for i in range(len(b)):
    b[i]=int(b[i])
# def nums(a,b):
s=Solution()
print(s.subsets(b))