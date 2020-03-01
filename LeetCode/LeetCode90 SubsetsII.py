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
        
        for i in range(len(nums)):
            startIndex = 0 # reset startIndex for each iteration
            
            # if duplicates found, work on startIndex
            if i > 0 and nums[i] == nums[i-1]:
                startIndex = endIndex + 1
            
            endIndex = len(subsets) - 1

            # loop for subsets
            for j in range(startIndex, endIndex+1):
                
                sets = list(subsets[j])
                sets.append(nums[i])
                subsets.append(sets)
        
        return subsets
nums = [1,2,2]
t = Solution()
print(t.subsetsWithDup(nums))
