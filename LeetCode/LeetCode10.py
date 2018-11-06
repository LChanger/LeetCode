class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls=len(s)
        lp=len(p)
        if lp==0 and ls!=0:return False
        i=j=0
        while i<ls:
        	if p[j]=="."or p[j]==s[i]:
        		j+=1
        		i+=1
        	elif p[j]=="*":
        		if j+1<lp:
        			if i+1<ls and p[j+1]==s[i+1]:
        				j+=2
        				i+=1
        			elif p[j+1]==s[i]:
        				j+=2
        		elif j==lp-1:return True
        		i+=1
        	else:return False
        	if j>=lp and i<ls:return False
        if j==lp:return True
    	else :return False
s="aaaabcd"
p="a*b.d"
t=Solution()
print (t.isMatch(s,p))   