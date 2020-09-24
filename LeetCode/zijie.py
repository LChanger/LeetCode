# abcd ,  词典：list， [a,bc,d,ab,cd]
def find_types(s,dic):
    if not s:return []
    res=[]
    def DFS(temp_s,path):
        if not temp_s:
            res.append(path)
            return
        for d in dic:
            if temp_s[:len(d)]==d:
                DFS(temp_s[len(d):],path+[d])
    DFS(s,[])
    return res
s="abcd"
# dic=["a","bc","d","ab","cd"]
dic=["ab","c","ab","d"]
print(find_types(s,dic))


