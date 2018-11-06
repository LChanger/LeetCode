class Solution(object):
    def isMatch(self):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        count=0
        for i in range(111111111,999999999):
        	x=i/100000
            y=i%100000
            if i%(x+y)==0:count+=1
        return count
# s="ab"
# p="c*a*b"
t=Solution()
print (t.isMatch())   