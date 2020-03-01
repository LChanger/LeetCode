class Solution:
    #方法一
    def jump(self, nums) -> int:
        #cur_end 是本轮跳转 所能跳到的最远距离，  cur_furest是下轮跳转所能跳到的最远距离
        cur_end=cur_furest=times=0
        for i in range(len(nums)):
            cur_furest=i+nums[i] if i+nums[i]>cur_furest else cur_furest
            if i==cur_end and cur_end!=len(nums)-1:
                cur_end=cur_furest
                times+=1
        return times
    #方法二  动态规划
    # dp[i][j]为 i到j的最小跳步 dp[i][j]=min(dp[i][k]+dp[k][j])
    # 画图可知 dp[i][j] 从右下角开始按行从左至右扫描 或从左上角开始按列从下到上扫描 本程序用第二种
    def jump2(self, nums) -> int:
        dp=[[len(nums) for i in range(len(nums)) ] for j in range(len(nums))]
        for j in range(0,len(nums)):
            dp[j][j]=0
            for k in range(j+1,min(len(nums),j+nums[j]+1)):
                dp[j][k]=1
        for j in range(1,len(nums)):
            for i in range(j-1,-1,-1):
                temp=dp[i][j]
                for k in range(i,min(j+1,i+nums[i]+1)):
                    if dp[i][k]+dp[k][j]<temp:
                        temp=dp[i][k]+dp[k][j]
                dp[i][j]=temp
        print(dp)
        return dp[0][len(nums)-1]
c=[2,3,1,1,4]
t=Solution()
print (t.jump(c))