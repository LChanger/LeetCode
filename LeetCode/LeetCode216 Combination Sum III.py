class Solution:
    def combinationSum3(self, k: int, n: int):
        res=[]
        def curCal(answer,target,start):#answer当前生成的组合序列，target目标数字，start 起始位置
            if len(answer)==k and target==0:
                res.append(answer)
                return
            for i in range(start,min(target+1,10)):
                curCal(answer+[i],target-i,i+1)
        curCal([],n,1)
        return res

t = Solution()
print(t.combinationSum3(3,9))
