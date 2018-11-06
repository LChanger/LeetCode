class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int

         if i+2*numRows-2*j!=i and i+2*numRows-2*j<n and flag==0:
	        	i=i+2*numRows-2*j
	        	ss=ss+s[i]
	        if i+2*j-2!=i and i+2*j-2<n and flag==1:
	        	i=i+2*j-2
	        	ss=ss+s[i]

        :rtype: str
        """
        n=len(s)
        if numRows==1:return s 
        j=1
        ss=""
        for i in range(0,n,2*numRows-2*j):
        	if i>=n or i<0:break
        	ss=ss+s[i]
        for j in range(2,numRows):
        	i=j-1
        	if i>=n or i<0:break
        	ss=ss+s[i]
        	flag=0
        	while min(i+2*numRows-2*j,i+2*j-2)<n:
        		fir=i+2*numRows-2*j
        		if  fir<numRows:break
	        	if flag==0:
	        		if fir>=n:break
		        	else:
		        		i=fir
		        		ss=ss+s[i]
		        		flag==1
	        	sec=i+2*j-2
	        	if sec<numRows:break
	        	else:
	        		if sec>=n:break
		        	else:
		        		i=sec
		        		ss=ss+s[i]
		        		flag==0
        	pass
        for i in range(numRows-1,n,2*numRows-2):
        	if i>=n or i<0:break
        	ss=ss+s[i]
        return ss
        
s="PAYPALISHIRING"
t=Solution()
print (t.convert(s,10))      
