class Solution:
    def maxProfit(self, k: int, prices) -> int:
        #buy[i][k]表示第i天持有股票进行了k次交易的收益
        #sell[i][k]表示第i天不持有股票进行了k次交易的收益
        buy=[[0]*(k+1) for i in range(len(prices))]
        sell=[[0]*(k+1) for i in range(len(prices))]
        buy[0][0]=-prices[0]
        buy[0][1]=-prices[0]
        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float("-inf")
        res=0
        k = min(k, len(prices)// 2)
        for i in range(1,len(prices)):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1,k+1):
                buy[i][j]=max(buy[i-1][j],sell[i-1][j]-prices[i])
                sell[i][j]=max(sell[i-1][j],buy[i-1][j-1]+prices[i])
                res=max(res,max(buy[i][j],sell[i][j]))
        return res
prices=[3,2,6,5,0,3]
k=2
print(Solution().maxProfit(k,prices))