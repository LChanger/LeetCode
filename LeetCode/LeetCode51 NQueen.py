class Solution:
    def solveNQueens(self, n: int):
        res=[]
        nums=[-1]*n #nums[i]代表在第i行上Q的位置
        self.dfs(nums,0,[],res)
        return res
    def dfs(self,nums,prog,path,res):#prog代表目前要探索的行数，path表示当前产生的图形（前prog-1行），res代表结果
        if prog==len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[prog]=i
            if self.valid(nums,prog):
                self.dfs(nums,prog+1,path+['.'*i+'Q'+'.'*(len(nums)-1-i)],res)
    def valid(self,nums,prog):
        for i in range(prog):
            if nums[prog]==nums[i] or abs(nums[prog]-nums[i])==abs(prog-i):return False
        return True
n=4
t=Solution()
print (t.solveNQueens(n))

#-------------------非常巧妙地剪枝算法----------
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         def explore(queens, xy_diff, xy_sum):
#             ind = len(queens)
#             if ind == n:
#                 res.append(queens)
#                 return
            
#             for t in range(n):
#                 if t not in queens and ind-t not in xy_diff and ind+t not in xy_sum:
#                     explore(queens+[t], xy_diff+[ind-t], xy_sum+[ind+t])
#         explore([], [], [])            
#         return [['.'*i + 'Q'+'.'*(n-i-1) for i in sol] for sol in res]