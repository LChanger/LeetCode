class Solution2:
	list1=[]
	res=[]
	def recurgenerate(self,first,last):
		if(first+1==last):
			self.list1[first],self.list1[last]='(',')'
			self.res.append("".join(self.list1))
			return 
		self.list1[first],self.list1[last]='(',')'
		self.recurgenerate(first+1,last-1)
		self.list1[first],self.list1[first+1]='(',')'
		self.recurgenerate(first+2,last)
		self.list1[last-1],self.list1[last]='(',')'
		self.recurgenerate(first,last-2)
		length=last-first+1
		if length%2==0:
			self.list1[first],self.list1[first+length/2-1]='(',')'
			self.recurgenerate(first+1,first+length/2-2)
			self.list1[first+length/2],self.list1[last]='(',')'
			self.recurgenerate(first+length/2+1,last-1)
		return 
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		self.list1=[]
		self.res=[]
		if n==0:return res
		self.list1=[None]*2*n
		self.recurgenerate(0,2*n-1)
		self.res=list(set(self.res))
		self.res.sort(key=self.res.index)
		return self.res
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p,left,right, parentheis=[]):
        	if left: generate(p+'(',left-1,right)
        	if right>left: generate(p+')',left,right-1)
        	if 0==right:parentheis.append(p)
        	return parentheis
        return generate('',n,n)