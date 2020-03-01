class Solution:
    def permuteUnique(self, nums):
        result=[]
        nums.sort()
        def recur(have,toadd):
            if len(toadd)==0:
                result.append(have)
                return
            for i in range(len(toadd)):
                if toadd[i-1:i]==toadd[i:i+1]:continue
                recur(have+[toadd[i]],toadd[0:i]+toadd[i+1:])
        recur([],nums)
        return result
c=[1,1,2]
t=Solution()
print (t.permuteUnique(c))