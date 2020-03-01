class Solution:
    def permute(self, nums):
        result=[]
        def recur(have,toadd):
            if len(toadd)==0:
                result.append(have)
                return
            for i in range(len(toadd)):
                recur(have+[toadd[i]],toadd[0:i]+toadd[i+1:])
        recur([],nums)
        return result

    # todo test
    def testList(self, nums):
        temp=nums[int(len(nums)/2):len(nums)]
        print(temp)
        del temp[0]
        print(temp)
        print(nums)
        return
    # 说明 + 操作 和截取操作 生成的都是一个新对象，而extend和append都是对原对象进行修改
    # [:]截取的是list列表   []是取出list元素
c=[1,2,3]
t=Solution()
print (t.permute(c))

print (t.testList(c))