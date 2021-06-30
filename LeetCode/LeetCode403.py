class Solution:
    def canCross(self, stones) -> bool:
        #记忆化搜索+二分查找
        if stones[1]-stones[0]>1:return False
        dp={}
        cache=set(stones)
        def helper(i,step):
            if i==stones[-1]:return True
            low=max(1,step-1)
            for j in range(low,step+2):
                if i+j not in cache:continue
                if (i+j,j) not in dp:
                    dp[(i+j,j)]=helper(i+j,j)
                if dp[(i+j,j)]:return True
            return False
        return helper(1,stones[1]-stones[0])
stones=[0,1,3,6,10,13,14]
print(Solution().canCross(stones))