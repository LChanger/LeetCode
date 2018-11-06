class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        t=st=0
        le=0
        while(t<len(s)):
        	i=1
        	while(t+i<len(s)):
        		temp=s[t:t+i].find(s[t+i])
        		if temp!=-1:break
        		i=i+1
        	if i>le:st,le=t,i
        	if t+i<len(s):t=t+temp+1
        	else:t=t+i
        s1=s[st:st+le]
        return (s1,le)
s="pwwkew"
#print s[2:4]
t=Solution()
print (t.lengthOfLongestSubstring(s))

