# 思路一：BFS问题 通过定义一个方向数组来控制方向直接相加或相减
class Solution:#DFS函数参数的定义不一样 此种方法是先判断是否相等再进入DFS函数
    def exist(self, board, word: str) -> bool:
        if word is None or len(board) == 0 or len(board[0]) == 0:
            return False
        m=len(board)#m*n的数组
        n=len(board[0])
        if len(word) > m*n:
            return False
        w_len=len(word)
        visit=[[False]*len(board[0]) for i in range(len(board))]

        def DFS(index,x,y):#index为word中将要寻找的字符，xy为当前位置已扫描完
            if index==w_len:
                return True
            if x+1<m and board[x+1][y]==word[index] and not visit[x+1][y]:
                visit[x+1][y]=True
                if DFS(index+1,x+1,y):return True
                visit[x+1][y]=False
            if x-1>=0 and board[x-1][y]==word[index] and not visit[x-1][y]:
                visit[x-1][y]=True
                if DFS(index+1,x-1,y):return True
                visit[x-1][y]=False
            if y+1<n and board[x][y+1]==word[index] and not visit[x][y+1]:
                visit[x][y+1]=True
                if DFS(index+1,x,y+1):return True
                visit[x][y+1]=False
            if y-1>=0 and board[x][y-1]==word[index] and not visit[x][y-1]:
                visit[x][y-1]=True
                if DFS(index+1,x,y-1):return True
                visit[x][y-1]=False
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visit[i][j]=True
                    if DFS(1,i,j):return True
                    visit[i][j]=False
        return False
# 思路一：BFS问题 通过定义一个方向数组来控制方向直接相加或相减
class Solution1:#DFS函数参数的定义不一样 此种方法是先进入函数再判断是否相等
    def exist(self, board, word: str) -> bool:
        if word is None or len(board) == 0 or len(board[0]) == 0:
            return False
        m=len(board)#m*n的数组
        n=len(board[0])
        if len(word) > m*n:
            return False
        w_len=len(word)
        visit=[[False]*len(board[0]) for i in range(len(board))]

        def DFS(index,x,y):#index为word中将要寻找的字符，xy为将要扫描的位置的xy坐标 这样可以节省代码
            if board[x][y]!=word[index] or visit[x][y]:return False
            visit[x][y]=True
            if index+1==w_len:return True
            if x+1<m and DFS(index+1,x+1,y):return True
            if x-1>=0 and DFS(index+1,x-1,y):return True
            if y+1<n and DFS(index+1,x,y+1):return True
            if y-1>=0 and DFS(index+1,x,y-1):return True
            visit[x][y]=False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and DFS(0,i,j):return True
        return False
# 思路二:BFS问题 通过定义一个方向数组来控制方向
#--------------------------以下答案原始问题------------------------
class Solution2:
    def exist(self, board, word: str) -> bool:
        w_len=len(word)
        direct=[
            [0,1],# right
            [1,0],# down
            [0,-1],# left
            [-1,0],# up
        ]
        def DFS(index,path,location):#cnt已经匹配到的字符个数,path走过的路径,location当前的位置 记录匹配字符的个数
            if index==w_len:return True
            for d in direct:
                next_loc=(location[0]+d[0],location[1]+d[1])
                if next_loc[0]>=len(board) or next_loc[1]>=len(board[0]):continue
                if next_loc[0]<0 or next_loc[1]<0:continue
                char=board[next_loc[0]][next_loc[1]]
                if char==word[index] and next_loc not in path and DFS(index+1,path+[next_loc],next_loc):
                    return True
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and DFS(1,[(i,j)],(i,j)):return True
        return False
#--------------------------以下答案为一个变种问题-------------------
#question：相邻顺序可以不同于word的顺序
class Solution3:
    def exist(self, board, word: str) -> bool:
        dic2={}#记录wrod字符及个数
        for i in word:
            dic2[i]=dic2.get(i,0)+1
        # left=right=0#左轴和右轴
        w_len=len(word)
        direct=[
            [0,1],# right
            [1,0],# down
            [0,-1],# left
            [-1,0],# up
        ]
        def DFS(cnt,path,location,dic1):#cnt已经匹配到的字符个数,path走过的路径,location当前的位置 记录匹配字符的个数
            if cnt==w_len:return True
            for d in direct:
                next_loc=(location[0]+d[0],location[1]+d[1])
                if next_loc[0]>=len(board) or next_loc[1]>=len(board[0]):continue
                if next_loc[0]<0 or next_loc[1]<0:continue
                char=board[next_loc[0]][next_loc[1]]
                if char in dic2 and next_loc not in path:
                    # while dic1.get(char,0)>=dic2[char]:
                    #     dic1[board[path[0]]]=dic1.get(board[path[0]],0)-1#回溯时减去对应的匹配字符
                    #     del path[0]
                    # else:
                    if dic1.get(char,0)<dic2[char]:
                        dic1[char]=dic1.get(char,0)+1#匹配字符加1
                        if DFS(cnt+1,path+[next_loc],next_loc,dic1):return True
                        dic1[char]=dic1.get(char,0)-1#回溯时减去对应的匹配字符
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dic2.get(board[i][j],0)>0 and DFS(1,[(i,j)],(i,j),{board[i][j]:1}):return True
        return False
board=[["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","a"],["a","a","a","b"]]

word ="aaaaaaaaaaaaaaaaaaaa"
t = Solution()
print(t.exist(board,word))
