class Solution:
    def partitionLabels(self, S: str):
        start=0
        end=len(S)-1
        res=[]
        cur=0
        cache={}#存储每个字符在列表中的最右位置
        max_len=0
        while cur<len(S):
            if cur>max_len:
                res.append(max_len-start+1)
                start=cur
                max_len=cur
            while S[cur] not in cache and end>=max(max_len,cur):
                if S[end] not in cache:
                    cache[S[end]]=end
                end-=1
            if S[cur] in cache:
                max_len=max(max_len,cache[S[cur]])
            cur+=1
        res.append(len(S)-start)
        return res
S="ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))