class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:return 0
        seqmap={}
        res=1
        for i in range(len(nums)):
            if nums[i] in seqmap:continue
            leftlen=seqmap.get(nums[i]-1,0)
            rightlen=seqmap.get(nums[i]-1,0)
            seqmap[nums[i]]=leftlen+rightlen+1
            #没有必要把nums[i]-leftlen 到 nums[i]+rightlen都进行更新，因为落在这里面的值不会对序列长度造成影响,直接continue了
            seqmap[nums[i]-leftlen]=leftlen+rightlen+1
            seqmap[nums[i]+rightlen]=leftlen+rightlen+1
            # for j in range(nums[i]-leftlen,nums[i]+rightlen+1):
            #     seqmap[j]=leftlen+rightlen+1
            res=max(res,seqmap[nums[i]])
        return res
nums=[100, 4, 200, 1, 3, 2]
s=Solution()
nums=input()
print(nums)
print(type(nums))
print(s.longestConsecutive(nums))