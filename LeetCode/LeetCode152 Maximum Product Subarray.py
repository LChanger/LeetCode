class Solution:
    def maxProduct(self, nums) -> int:
        maxpro=nums[0]
        pos=neg=nums[0]
        #保留一个最大的和一个最小的
        for i in range(1,len(nums)):
            pos,neg=max(pos*nums[i],neg*nums[i],nums[i]),min(pos*nums[i],neg*nums[i],nums[i])
            maxpro=max(maxpro,pos)
        return maxpro
    #----------------Time Limit Exceeded------------
    # def maxProduct(self, nums) -> int:
    #     maxpro=max(nums)
    #     dp=[]
    #     for i in range(len(nums)):
    #         for j in range(len(dp)):
    #             dp[j]=dp[j]*nums[i]
    #         dp.append(nums[i])
    #         maxpro=max(maxpro,max(dp))
    #     return maxpro
    #----------------Memory Limit Exceeded------------
    # def maxProduct(self, nums) -> int:
    #     # start=end=0#两个指针
    #     maxpro=max(nums)
    #     dp=[[0]*len(nums) for i in range(len(nums))]
    #     for j in range(0,len(nums)):dp[0][j]=nums[j]
    #     for j in range(1,len(nums)):
    #         for i in range(1,j+1):
    #             dp[i][j]=dp[0][j]*dp[i-1][j-1]
    #             maxpro=max(dp[i][j],maxpro)
    #     return maxpro
n=[2,3,-2,4]
t=Solution()
print (t.maxProduct(n))