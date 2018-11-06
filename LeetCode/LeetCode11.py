class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s=0
        i=0
        j=len(height)-1
        while i<=j:
        	if height[i]<height[j]:
        		if height[i]*(j-i)>s:
        			s=height[i]*(j-i)
        		i+=1
        	else:
        		if height[j]*(j-i)>s:
        			s=height[j]*(j-i)
        		j-=1
        return s
height=[2,2,2]
t=Solution()
print(t.maxArea(height))