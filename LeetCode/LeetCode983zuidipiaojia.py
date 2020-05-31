#思路：背包问题 dp[i]表示days[:i+1]用的最少花费
#
class Solution:
    def mincostTickets(self, days, costs) -> int:
        if not days:return 0
        #查找小于等于target的第一个数
        def binarySearch(low,high,target):
            while low<high:
                mid=(low+high+1)//2
                if days[mid]<=target:
                    low=mid
                else:high=mid-1
            if target>=days[low]:return low
            return -1
        term=[1,7,30]
        dp=[costs[0]]
        for i in range(1,len(days)):
            temp=dp[i-1]+min(costs)
            before7=binarySearch(0,i-1,days[i]-7)
            val7=0 if before7==-1 else dp[before7]
            temp=min(temp,val7+costs[1])
            before30=binarySearch(0,i-1,days[i]-30)
            val30=0 if before30==-1 else dp[before30]
            temp=min(temp,val30+costs[2])
            dp.append(temp)
        return dp[-1]
days = [1,4,6,7,8,20] 
costs = [7,2,15]
s=Solution()
print(s.mincostTickets(days,costs))