# 思路二：应用84题中的技巧，按行扫描，计算目前的最大面积，若有0该列被截断
# 计算目前最大面积的算法：定义一个栈，栈内存储所有的比栈顶元素值都小的值的 位置， 为递增序列
# 当 扫描的元素小于栈顶元素时，将栈顶元素取出，开始计算栈顶元素为水平线的 区域面积
# 此处边界处理非常巧妙
#----------------------O（n²） time limited--------------------
class Solution:
    def maximalRectangle(self, matrix) -> int:
        m=len(matrix)
        if m==0:return 0
        n=len(matrix[0])
        maxarea=0
        dp=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    dp[j]+=1
                else:dp[j]=0
            maxarea=max(self.largestRectangleArea(dp),maxarea)
        return maxarea
    def largestRectangleArea(self, heights) -> int:
        res=0
        stack=[-1]
        for i,v in enumerate(heights+[-1]):#当扫描到最后时一定会清栈，且最后是 负值  即-1*数组长度， 不影响最优结果
            while stack and stack[-1]>-1 and heights[stack[-1]]>v:#因为此时元素比栈顶小，所以计算以栈顶元素为最高水平线的面积
                res=max(res,heights[stack.pop()]*(i-1-stack[-1]))
            #此时heights[stack[-1]]<=v
            stack.append(i)
        return res
S = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
t = Solution()
print(t.maximalRectangle(S))
