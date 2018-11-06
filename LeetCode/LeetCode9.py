class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if abs(x)>2147483648:return 0
        fuhao=1
        if x<0:
        	fuhao=-1
        	x=-x
        xx=x
        y=temp=0
        while x>0:
        	y*=10;
        	temp=x%10;
        	x/=10;
        	y=y+temp;
        	#if y>2147483648:return 0
        if y*fuhao==xx:return True
        return False
s=121
t=Solution()
print (t.isPalindrome(s))  