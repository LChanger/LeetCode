class Solution:
    def partition(self, s: str):
        #dp[i][j]表示s[i:j]是否是回文串
        dp=[[False]*(len(s)+1) for i in range(len(s)+1)]
        dp[len(s)][len(s)]=True
        for i in range(len(s)-1,-1,-1):
            dp[i][i+1]=True
            dp[i][i]=True
            for j in range(i+2,len(s)+1):
                if s[j-1]==s[i] and dp[i+1][j-1]:
                    dp[i][j]=True
        ans=[]

        def recur_dfs(start,substr):
            if start>=len(s):
                ans.append(substr)
                return
            for i in range(start,len(s)):
                if dp[start][i+1]:
                    recur_dfs(i+1,substr+[s[start:i+1]])
        recur_dfs(0,[])
        return ans
print(Solution().partition("aab"))