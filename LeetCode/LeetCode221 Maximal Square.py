# 思路一:同时向右，下，右下三个方向探索，探索过的位置翻转为2,下一次的起始点不从该点开始
class Solution1:
    def maximalSquare(self, matrix) -> int:
        maxSquare=0
        m=len(matrix)
        if m==0:return 0
        n=len(matrix[0])
        def judgeSquare(i,j):
            x,y=i,j
            while i+1<m and j+1<n:
                breakflag=1
                for ii in range(i+1,x-1,-1):
                    if matrix[ii][j+1]=="0":
                        breakflag=0
                        break
                for jj in range(j+1,y-1,-1):
                    if matrix[i+1][jj]=="0":
                        breakflag=0
                        break
                if breakflag==0:break
                # for ii in range(i+1,x-1,-1):matrix[ii][j+1]="2"
                # for jj in range(j+1,y-1,-1):matrix[i+1][jj]="2"
                i+=1
                j+=1
            return (i-x+1)*(i-x+1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":maxSquare=max(maxSquare,judgeSquare(i,j))
        return maxSquare
# 思路二:动态规划法，dp[i][j]代表以（i,j）点为右下点的最大正方形边长
# dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
# 对dp 算法进行修改，将二维数组改为一维数组 由temp来保存 dp[i-1][j-1]
class Solution:
    def maximalSquare(self, matrix) -> int:
        m=len(matrix)
        if m==0:return 0
        n=len(matrix[0])
        dp=[int(i) for i in matrix[0]]
        max_l=max(dp)
        for i in range(1,m):
            pre=dp[0]
            dp[0]=int(matrix[i][0])
            max_l=max(dp[0],max_l)
            for j in range(1,n):
                temp=dp[j]#
                if matrix[i][j]=="0":dp[j]=0
                else:
                    dp[j]=min(pre,min(dp[j],dp[j-1]))+1
                    max_l=max(dp[j],max_l)
                pre=temp#作为下一个循环的 dp[i-1][j-1]
        return max_l*max_l
S =[
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]]
t = Solution()
print(t.maximalSquare(S))
