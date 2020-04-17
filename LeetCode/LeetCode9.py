class Solution1(object):
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
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False
        if x<10:return True
        digit=2
        while x//(10**digit)!=0:digit+=1
        for i in range(1,digit//2+1):
            if x//pow(10,i-1)%10!=x//pow(10,digit-i)%10:return False
        return True
s=121
t=Solution()
print (t.isPalindrome(s))  