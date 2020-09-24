#思路：DFS
#T：O()
#S：O(333)
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set([str(i) for i in range(1,10)]) for i in range(9)]#记录横轴可用元素
        cols=[set([str(i) for i in range(1,10)]) for i in range(9)]#记录纵轴可用元素
        ninesum=[[set([str(i) for i in range(1,10)]) for i in range(3)] for j in range(3)]#记录九宫格可用元素
        null_set=[]#记录空格位置
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    null_set.append((i,j))
                else:
                    rows[i].remove(board[i][j])
                    cols[j].remove(board[i][j])
                    ninesum[i//3][j//3].remove(board[i][j])
        #获得x,y位置的可用元素
        def getpossiblity(x,y):
            return (rows[x])&(cols[y])&(ninesum[x//3][y//3])
        #获得每个空位置的候选元素集合
        rest=[getpossiblity(i,j) for i,j in null_set]
        #选择排序,按候选个数从小到大排序，为了使DFS时减少回溯
        for i in range(len(null_set)):
            k=i
            for j in range(i,len(null_set)):
                if len(rest[k])>len(rest[j]):k=j
            rest[i],rest[k]=rest[k],rest[i]
            null_set[i],null_set[k]=null_set[k],null_set[i]
        def recurDFS(start):
            if start==len(null_set):return True
            x,y=null_set[start]
            poss=getpossiblity(x,y)
            for num in poss:
                board[x][y]=num
                rows[x].remove(num)
                cols[y].remove(num)
                ninesum[x//3][y//3].remove(num)
                if recurDFS(start+1):return True
                rows[x].add(num)
                cols[y].add(num)
                ninesum[x//3][y//3].add(num)
                board[x][y]='.'
            return False
        return recurDFS(0)
                
#-------------------------------第一版本
class Solution1:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        ninesum=[[set() for i in range(3)] for j in range(3)]
        null_set=[]
        nums=[str(i) for i in range(1,10)]
        nums=set(nums)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    null_set.append((i,j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    ninesum[i//3][j//3].add(board[i][j])
        def getpossiblity(x,y):
            return (nums-rows[x])&(nums-cols[y])&(nums-ninesum[x//3][y//3])
        #每个位置的候选元素
        rest=[getpossiblity(i,j) for i,j in null_set]
        #选择排序,按候选个数从小到大
        for i in range(len(null_set)):
            k=i
            for j in range(i,len(null_set)):
                if len(rest[k])>len(rest[j]):k=j
            rest[i],rest[k]=rest[k],rest[i]
            null_set[i],null_set[k]=null_set[k],null_set[i]
        def recurDFS(start):
            if start==len(null_set):return True
            x,y=null_set[start]
            poss=getpossiblity(x,y)
            for num in poss:
                board[x][y]=num
                rows[x].add(num)
                cols[y].add(num)
                ninesum[x//3][y//3].add(num)
                if recurDFS(start+1):return True
                rows[x].remove(num)
                cols[y].remove(num)
                ninesum[x//3][y//3].remove(num)
                board[x][y]='.'
            return False
        return recurDFS(0)
        
s=Solution()
board=[
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)