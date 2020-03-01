class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count=0
        i=1
        while n//i!=0:
            cur=(n//i)%i
            bef=n//i//10
              aft=n%i
            if cur==0:count+=bef*i
            elif cur==1:count+=(bef*i+aft+1)
            else:count+=(bef*i+i)
            i*=10
        return count
s=Solution()
print(s.NumberOf1Between1AndN_Solution(1))