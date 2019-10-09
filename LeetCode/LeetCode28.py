# Definition for singly-linked list.
needle="bba"
haystack = "aaaaa"
# 思路，纸面上画一下每步的步骤
class Solution:
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

t = Solution()
t.strStr(haystack,needle)
