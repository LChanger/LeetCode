class UnionFindSet:
    def __init__(self, nodes):
        # 生成父节点字典  pre[i]=j代表i节点的父节点是j 
        self.pre={}
        self.category={}#类别
        self.rank={}#树的深度
        for n in nodes:
            self.pre[n]=n
            self.category[n]={n}
            self.rank[n]=0
    def find(self,node):
        #寻找根节点
        root=node
        while self.pre[root]!=root:root=self.pre[root]
        #路径压缩，此时root为根节点
        while node!=root:
            p=self.pre[node]#临时存储父节点
            self.pre[node]=root#将此节点的全部父节点都直接指向根节点
            node=p
        return root
    def union(self,node1,node2):
        p1=self.find(node1)
        p2=self.find(node2)
        if p1!=p2:
            if self.rank[p1]<self.rank[p2]:#深度低的树连到深度高的树上
                self.pre[p1]=p2
                self.category[p2]=self.category[p2].union(self.category.pop(p1))
            else:
                self.pre[p2]=p1
                if self.rank[p1]==self.rank[p2]:
                    self.rank[p1]+=1
                self.category[p1]=self.category[p1].union(self.category.pop(p2))
class Solution:
    def classify(self, termPair):
        '''
        termPair:List[tuple]
        本质上此题是一个 求无向图中所有连通分量 的问题。
        采用并查集实现。
        '''
        nodes=set()
        for n1,n2 in termPair:
            nodes.add(n1)
            nodes.add(n2)
        u=UnionFindSet(nodes)
        for n1,n2 in termPair:
            u.union(n1,n2)
        res=[]
        for v in u.category.values():
            res.append(v) 
        return res
term=[
    ("苹果","梨"),
    ("汽车","火车"),
    ("北京","南京"),
    ("苹果","香蕉"),
    ("上海","南京"),
    ("汽车","马车"),
    ("西瓜","香蕉")
]
s=Solution()
print(s.classify(term))