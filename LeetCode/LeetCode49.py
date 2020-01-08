class Solution:
    def groupAnagrams(self, strs):
        dic={}
        for i in range(len(strs)):
            key= "".join((lambda x:(x.sort(),x)[1])(list(strs[i])))# 对string 进行排序
            if key not in dic:dic[key]=[strs[i]]
            else:dic[key].append(strs[i])
        res=[]
        for key in dic:
            res.append(dic[key])
        return res
c=["eat", "tea", "tan", "ate", "nat", "bat"]
t=Solution()
print (t.groupAnagrams(c))