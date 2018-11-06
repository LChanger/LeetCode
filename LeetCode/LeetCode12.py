class Solution(object):
    alphbet1=['I','II','III','IV','V','VI','VII','VIII','IX']
    alphbet2=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    alphbet3=['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    alphbet4=['M','MM','MMM']
    alphbet=[alphbet1,alphbet2,alphbet3,alphbet4]
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s=''
        temp=i=0
        while num>0:
        	temp=num%10
        	if temp!=0:
        		s=Solution.alphbet[i][temp-1]+s
        	num/=10
        	i+=1
        return s 
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        for i in range():
        	for j in range(len(Solution.alphbet[i])-1,-1,-5):
        		if Solution.alphbet[i][j] in s:
        			x-=pow(10,i)*2
        			break
        for count in range(len(s)):
        	if(s[count]=='M'):x+=1000
        	if(s[count]=='D'):x+=500
        	if(s[count]=='C'):x+=100
        	if(s[count]=='L'):x+=50
        	if(s[count]=='X'):x+=10
        	if(s[count]=='V'):x+=5
        	if(s[count]=='I'):x+=1
       
        # for j in range(8,-1,-1):
        # 	if Solution.alphbet[2][j] in s:
        # 		x+=pow(10,i)*(j+1)
        # 	break
        return x
x=3765
s="XXX"
t=Solution()
print (t.intToRoman(x))   
print (t.romanToInt(t.intToRoman(x)))   