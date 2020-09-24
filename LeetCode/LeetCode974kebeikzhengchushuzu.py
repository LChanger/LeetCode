#思路：dp[i][j]代表以A[i]结尾的可被k整除余j的子数组数目，dp[i][j]=dp[i-1][(K+j-A[i]%K)%K]
#T:O(NK)
#S:O(k)
# class Solution:
#     def subarraysDivByK(self, A, K: int) -> int:
#         if not A:return 0
#         dp=[0]*K
#         dp[A[0]%K]=1
#         res=dp[0]
#         for i in range(1,len(A)):
#             temp=[0]*K
#             for j in range(K):
#                 temp[j]=dp[(K+j-A[i]%K)%K]
#                 if j==A[i]%K:temp[j]+=1
#             dp.clear()
#             dp=temp
#             res+=dp[0]
#         return res

#思路：前缀和
#T:O(NK)
#S:O(k)
class Solution:
    def subarraysDivByK(self, A, K: int) -> int:
        if not A:return 0
        map_cnt={0:1}
        pre=0# pre[i]前i项和
        res=0
        for i in range(len(A)):
            pre+=A[i]
            pre=pre%K
            res+=map_cnt.get(pre,0)
            map_cnt[pre]=map_cnt.get(pre,0)+1
        return res
A=[4,5,0,-2,-3,1]
K=5
print(Solution().subarraysDivByK(A,5))