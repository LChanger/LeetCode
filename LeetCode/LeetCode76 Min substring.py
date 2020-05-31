# 思路:用一个字典来记录所有子串的字符及数量
# 记录两个轴，当配对个数正好相等时，根据窗口大小更新两个轴
class Solution1:
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
#思路：维护一个字典用于记录T的键值对应的个数
#另外维护一个字典记录双指针中间的键值对应的个数
#若快指针扫描的字符已在等于慢指针且已超过对应个数，则向前步进
#T:O(N^1.5)
#S:O(1)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        dic_t=collections.defaultdict(int)
        dic_s=collections.defaultdict(int)
        index=collections.deque()
        for i in t:
            dic_t[i]+=1
        start=0
        end=len(s)
        cnt=0#有效匹配个数
        for i in range(len(s)):
            if s[i] in dic_t:
                dic_s[s[i]]+=1
                if dic_s[s[i]]<=dic_t[s[i]]:cnt+=1
                index.append(i)
                while index and dic_s[s[index[0]]]>dic_t[s[index[0]]]:
                    dic_s[s[index[0]]]-=1
                    index.popleft()
                if cnt==len(t) and index and i-index[0]<end-start:
                    start=index[0]
                    end=i
        return s[start:end+1] if end!=len(s) else ""   
S = "ADOBECODEBANC"
T = "ABC"
t = Solution()
print(t.minWindow(S,T))
