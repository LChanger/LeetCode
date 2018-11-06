class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x)>2147483648:return 0
        fuhao=1
        if x<0:
        	fuhao=-1
        	x=-x
        y=temp=0
        while x>0:
        	y*=10;
        	temp=x%10;
        	x/=10;
        	y=y+temp;
        	if y>2147483648:return 0
        return y*fuhao
x=-787465
t=Solution()
print (t.reverse(x))   