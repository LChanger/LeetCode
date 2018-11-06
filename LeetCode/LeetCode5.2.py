class Solution(object):
    def longestPalindrome(self, s):
        """
		n+1<length and 
        or n+i+1>=length 
        :type s: str
        :rtype: str
        """
        length=len(s)
        i=st=end=n=0
        k=1
        while n<length-k/2:
        	if n+1<length and s[n]==s[n+1]:
        		i=0
        		while n-i>=0 and n+i+1<length:
        			if s[n-i]!=s[n+1+i]:break
        			i+=1
        		i-=1
        		if 2*i+2>k:st,end,k=n-i,n+1+i,2*i+2
        	if n>0 and n+1<length and s[n-1]==s[n+1]:
        		i=0
        		while n-i>=0 and n+i<length:
        			if s[n-i]!=s[n+i]:break
        			i+=1
        		i-=1
        		if 2*i+1>k:st,end,k=n-i,n+i,2*i+1
        	n+=1
        return s[st:end+1],k
s="babaddtattarrattatddetartrateedredividerb"
t=Solution()
print (t.longestPalindrome(s))       	