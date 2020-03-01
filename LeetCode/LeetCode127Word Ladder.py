import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not wordList:return 0
        def isTransformation(preword,nextword):
            num=0
            for i in range(len(preword)):
                if preword[i]!=nextword[i]:num+=1
            if num!=1:return False
            return True
        length=0
        i=0
        queue=collections.deque([beginWord])
        while queue:
            layer=len(queue)
            length+=1
            while layer>0:
                top=queue.popleft()
                if top==endWord:return length
                for i in range(len(wordList)-1,-1,-1):
                    if isTransformation(top,wordList[i]):queue.append(wordList.pop(i))
                layer-=1
        return 0
# --------------------------双向检索 126------------------------------

class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        tree,words,n=collections.defaultdict(set),set(wordList),len(beginWord)
        if endWord not in wordList: return []
        found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in eq: 
                            found = True
                        else: 
                            nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq): 
                bq, eq, rev = eq, bq, not rev
        def bt(x):
            return [[x]] if x==endWord else [[x]+rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)
beginWord = "hit"
endWord = "cog"
wordList =["hot","dot","dog","lot","log","cog","dag"]
t = Solution1()
print(t.findLadders(beginWord,endWord,wordList))