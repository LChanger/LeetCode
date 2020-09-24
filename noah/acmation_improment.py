class Node:
    def __init__(self,val):
        self.val=val
        self.fail=None
        self.tail=0
        self.child={}#子结点

class Acmation:
    def __init__(self):
        self.root=Node("")
        self.count=0
        self.strs={}
    
    def insert(self,ch):
        node=self.root
        for c in ch:
            if c not in node.child:
                new_node=Node(c)
                node.child[c]=new_node
            node=node.child[c]
        self.count+=1
        node.tail=self.count
        self.strs[node.tail]=ch
    #修改fail指针
    def ac_automation(self):
        self.root.fail=None
        from collections import deque
        que=deque()
        for child in self.root.child.values():
            child.fail=self.root
            que.append(child)
        while que:
            top=que.popleft()
            for c,v in top.child.items():
                fail_to=top.fail
                while fail_to:
                    if c in fail_to.child:
                        v.fail=fail_to.child[c]
                        break
                    else:
                        fail_to=fail_to.fail
                if not fail_to:v.fail=self.root
                que.append(v)
        
    #进行模式匹配
    def runkmp(self,str_mode):
        p=self.root#s字符与p的子结点匹配
        from collections import defaultdict
        cnt=defaultdict(list)
        i=0
        while i<len(str_mode):
            if str_mode[i] in p.child:
                p=p.child[str_mode[i]]
                temp=p
                while temp:
                    if temp.tail>0:
                        equal=self.strs[temp.tail]
                        cnt[equal].append(i-len(equal)+1)
                    temp=temp.fail
                i+=1
            else:
                p=p.fail
                if not p:
                    p=self.root
                    i+=1
        return cnt

key = ["王志","王志青","dahai","qww"]        #创建模式串
acp = Acmation()

for s in key:
    acp.insert(s)                           #添加模式串
import datetime

acp.ac_automation()

start = datetime.datetime.now()             #开始时间

text = '王志喜欢王志青'
d = acp.runkmp(text)                    #运行自动机
# '''
print (d)                               #打印
for i in d.keys():
    print(i,d[i])                #将子串匹配的位置显示
# '''
end  = datetime.datetime.now()              #结束时的时间
print ('总共花费时间是:',end - start)       #打印出总共花费时间
