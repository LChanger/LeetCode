# 思路一：每个元素定义两个指针向前向后扫描直至小于（被截断）停止，然后记录该区域值
#----------------------O（n²） time limited--------------------
class Solution1:
    def largestRectangleArea(self, heights) -> int:
        res=0
        for i in range(len(heights)):
            m,n=i,i
            while m<len(heights) and heights[m]>=heights[i]:m+=1
            while n>-1 and heights[n]>=heights[i]:n-=1
            area=heights[i]*(m-1-n)
            res=max(area,res)
        return res

# 思路二：定义一个栈，栈内存储所有的比栈顶元素值都小的值的 位置， 为递增序列
# 当 扫描的元素小于栈顶元素时，将栈顶元素取出，开始计算栈顶元素为水平线的 区域面积
# 此处边界处理非常巧妙
#----------------------O（n²） time limited--------------------
class Solution:
    def largestRectangleArea(self, heights) -> int:
        res=0
        stack=[-1]
        for i,v in enumerate(heights+[-1]):#当扫描到最后时一定会清栈，且最后是 负值  即-1*数组长度， 不影响最优结果
            while stack and stack[-1]>-1 and heights[stack[-1]]>v:#因为此时元素比栈顶小，所以计算以栈顶元素为最高水平线的面积
                res=max(res,heights[stack.pop()]*(i-1-stack[-1]))
            #此时heights[stack[-1]]<=v
            stack.append(i)
        return res
S = [2,1,5,6,2,3]
t = Solution()
print(t.largestRectangleArea(S))
