class Solution:
    def totalNQueens(self, n: int) -> int:
        res=[0]
        def dfs(queens,xy_diff,xy_num):
            le=len(queens)
            if le==n:
                res[0]+=1
                return
            for i in range(n):
                if i not in queens and le-i not in xy_diff and le+i not in xy_num:
                    dfs(queens+[i],xy_diff+[le-i],xy_num+[le+i])
        dfs([],[],[])
        return res[0] 
n=4
t=Solution()
print (t.totalNQueens(n))