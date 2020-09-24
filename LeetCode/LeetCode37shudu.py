class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #思路：DFS
        matrix=[[{'1','2','3','4','5','6','7','8','9'} for j in range(3)] for i in range(3)]
        row=[{'1','2','3','4','5','6','7','8','9'} for i in range(9)]
        col=[{'1','2','3','4','5','6','7','8','9'} for i in range(9)]
        to_visited=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    to_visited.append((i,j))
                else:
                    row[i].remove(board[i][j])
                    col[j].remove(board[i][j])
                    matrix[i//3][j//3].remove(board[i][j])
        def DFS(start):
            if start==len(to_visited):
                return True
            i,j=to_visited[start]
            options=row[i]&col[j]&matrix[i//3][j//3]
            for x in options:
                board[i][j]=x
                row[i].remove(x)
                col[j].remove(x)
                matrix[i//3][j//3].remove(x)
                if DFS(start+1):
                    return True
                board[i][j]='.'
                row[i].add(x)
                col[j].add(x)
                matrix[i//3][j//3].add(x)
            return False
        DFS(0)
        return None
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print(board)