#思路：构造并查集，当同一个子集中的两个元素不相等时，则返回False
class UnionFindSet:
    def __init__(self,char_set):
        self.pre={}#记录父节点
        self.rank={}#记录深度
        for ch in char_set:
            self.pre[ch]=ch
            self.rank[ch]=1
    def find(self,ch):
        root=ch
        while self.pre[root]!=root:
            root=self.pre[root]
        #路径压缩
        while ch!=root:
            temp=self.pre[ch]
            self.pre[ch]=root
            ch=temp
        return root
    def union(self,ch1,ch2):
        if self.rank[ch1]==self.rank[ch2]:
            self.pre[ch2]=ch1
            self.rank[ch1]+=1
        elif self.rank[ch1]<self.rank[ch2]:
            self.pre[ch1]=ch2
        else:
            self.pre[ch2]=ch1
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ch_set=set()
        e_list=[]
        ne_list=[]
        for equal in equations:
            ch_set.add(equal[0])
            ch_set.add(equal[3])
            if equal[1]=='=':e_list.append(equal)
            else:ne_list.append(equal)
        u=UnionFindSet(ch_set)
        for equal in e_list:
            root1=u.find(equal[0])
            root2=u.find(equal[-1])
            if root1!=root2:
                u.union(root1,root2)
        for equal in ne_list:
            root1=u.find(equal[0])
            root2=u.find(equal[-1])
            if root1==root2:return False
        return True
equations=["a==b","b!=a"]
print(Solution().equationsPossible(equations))