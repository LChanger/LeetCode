#思路：双向扫描
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        words=set(wordList)
        if endWord not in words:return []
        bq=set()
        eq=set()
        found=False
        bq.add(beginWord)
        eq.add(endWord)
        length=len(beginWord)
        from collections import defaultdict
        tree=defaultdict(set)
        is_reverse=False
        while bq and not found:
            words-=bq#删除已访问过得
            next_bq=set()
            for start_word in bq:
                for i in range(length):
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        next_word=start_word[:i]+c+start_word[i+1:]
                        if next_word in words:
                            if not is_reverse:
                                tree[start_word].add(next_word)
                                next_bq.add(next_word)
                            else:
                                tree[next_word].add(start_word)
                                next_bq.add(start_word)
                        if next_word in eq:
                            found=True
                            break
            bq=next_bq
            bq,eq=eq,bq
            is_reverse=not is_reverse
        if not found:return []
        res=[]
        def BFS(path,cur_word):
            if cur_word==endWord:
                return res.append(path)
            for next_word in tree[cur_word]:
                BFS(path+[next_word],next_word)
        BFS([beginWord],beginWord)
        return res

#思路：单向扫描
class Solution0:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        words=set(wordList)
        if endWord not in words:return []
        bq=set()
        found=False
        bq.add(beginWord)
        length=len(beginWord)
        from collections import defaultdict
        tree=defaultdict(set)
        while bq and not found:
            words-=bq#删除已访问过得
            next_bq=set()
            for start_word in bq:
                for i in range(length):
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        next_word=start_word[:i]+c+start_word[i+1:]
                        if next_word in words:
                            tree[start_word].add(next_word)
                            next_bq.add(next_word)
                        if next_word==endWord:
                            found=True
                            break
            bq=next_bq
        if not found:return []
        res=[]
        def BFS(path,cur_word):
            if cur_word==endWord:
                return res.append(path)
            for next_word in tree[cur_word]:
                BFS(path+[next_word],next_word)
        BFS([beginWord],beginWord)
        return res
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(Solution().findLadders(beginWord,endWord,wordList))