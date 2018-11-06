class Solution(object):
    def longestPalindrome(self, s):
        """
		n+1<length and 
        or n+i+1>=length 
        :type s: str
        :rtype: str
        """
        length=len(s)
        i=st=end=m=n=0
        k=1
        while m<length-k:
        	#n=m
        	#flag1=flag2=flagn=flagm=1
        	while 2*n<length+m:
        		if n+1<length and s[n]==s[n+1]:
        			for i in range(0,n-m+1):
        				if n-i<0 or n+i+1>=length or s[n-i]!=s[n+1+i]:break
        			else:
        				if 2*i+2>k:st,end,k=m,n+1+i,2*i+2
        		if n>0 and n+1<length and s[n-1]==s[n+1]:
        			for i in range(0,n-m+1):
        				if n-i<0 or n+i>=length or s[n-i]!=s[n+i]:break
        			else:
        				if 2*i+1>k:st,end,k=m,n+i,2*i+1
        		n+=1
        	n-=1
        	m=m+1
        return s[st:end+1],k
s="bddtattarrattatddetartrateedredividerb"
t=Solution()
print (t.longestPalindrome(s))       	