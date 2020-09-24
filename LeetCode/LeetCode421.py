#思路：前缀树
class Solution:
    def findMaximumXOR(self, nums) -> int:
        trie={}
        L=len(str(bin(max(nums))))-2
        nums_bit=[[(num>>i)&1 for i in range(L)][::-1] for num in nums]
        res=0
        for bits in nums_bit:
            temp=trie
            search=trie
            cur_xor=0
            #构造前缀树+搜索
            for bit in bits:
                if 1-bit in search:
                    cur_xor=(cur_xor<<1)+1
                    search=search[1-bit]
                elif bit in search:
                    cur_xor=cur_xor<<1
                    search=search[bit]
                if bit not in temp:
                    temp[bit]={}
                temp=temp[bit]
            res=max(res,cur_xor)
        return res
nums=[1]
print(Solution().findMaximumXOR(nums))