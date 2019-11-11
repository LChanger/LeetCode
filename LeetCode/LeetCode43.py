class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n2=int(num2)
        product=0
        i=0
        for i in range(len(num1)-1,-1,-1):
            product+=int(num1[i])*n2*pow(10,len(num1)-1-i)
            i+=1
        return str(product)

c="123"
x="456"
t=Solution()
print (t.multiply(c,x))