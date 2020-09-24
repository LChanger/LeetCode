class Solution0:
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

#思路：一个list path[i]表示第i行的列位置
#xy_add 记录 当前行 加 列的位置，用于识别右下方向的冲突位置。
#xy_sub 记录 当前行 减 列的位置，用于识别左下方向的冲突位置。
class Solution:
    def solveNQueens(self, n: int) :
        if not n:return []
        res=[]
        def DFS(path,length,xy_add,xy_sub):
            if length==n:return res.append(path)
            for i in range(n):
                if i not in path and length+i not in xy_add and length-i not in xy_sub:
                    DFS(path+[i],length+1,xy_add|{length+i},xy_sub|{length-i})
        DFS([],0,set(),set())
        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j]='.'*res[i][j]+'Q'+'.'*(len(res[i])-1-res[i][j])
        return res
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