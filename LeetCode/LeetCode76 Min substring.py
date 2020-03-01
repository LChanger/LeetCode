# 思路:用一个字典来记录所有子串的字符及数量
# 记录两个轴，当配对个数正好相等时，根据窗口大小更新两个轴
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic2={}#记录子串字符及个数
        for i in t:
            dic2[i]=dic2.get(i,0)+1
        # left=right=0#左轴和右轴
        cnt=0#合理匹配的个数
        index=[]# 当前 匹配的字符的位置
        res=s+'!'#记录最优子串
        dic1={}#记录匹配字符的个数
        for i in range(len(s)):
            if s[i] in dic2:
                index.append(i)
                dic1[s[i]]=dic1.get(s[i],0)+1
                if dic1[s[i]]<=dic2[s[i]]:cnt+=1
                while dic1[s[index[0]]]>dic2[s[index[0]]]: 
                    dic1[s[index[0]]]-=1
                    del index[0] #将左轴向右移
                if cnt==len(t) and index[-1]-index[0]+1<len(res):
                    res=s[index[0]:index[-1]+1]
        return "" if res==s+'!' else res
S = "abc"
T = "ac"
t = Solution()
print(t.minWindow(S,T))
