# Definition for singly-linked list.
needle="bba"
haystack = "aaaaa"
# 思路，纸面上画一下每步的步骤
class Solution0:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            if len(haystack)==0:return 0
            return -1
        def kmp(needle):
            next=[-1,]
            k=-1
            j=1
            while j<len(needle):
                while k!=-1 and needle[j-1]!=needle[k]:k=next[k]
                k+=1
                next.append(k)
                j+=1
            return next
        next=kmp(needle)
        i=j=0
        while i+len(needle)-j-1<len(haystack):
            if j==-1:
                i+=1
                j=0
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j=next[j]
            if j==len(needle):return i-j
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #kmp算法
        next=[-1]*len(needle)
        for i in range(len(needle)-1):
            temp=next[i]
            while temp!=-1 and needle[temp]!=needle[i]:
                temp=next[temp]
            next[i+1]=temp+1
        # return next
        i=0
        j=0
        while i<len(haystack) and j<len(needle):
            if j==-1:
                i+=1
                j=0
            if haystack[i]==needle[j]:
                j+=1
                i+=1
            else:
                j=next[j]

        if j==len(needle):return i-len(needle)
        return -1
        
t = Solution()
t.strStr(haystack,needle)
