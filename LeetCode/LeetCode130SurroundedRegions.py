class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:return []
        rows=len(board)
        cols=len(board[0])
        from collections import deque
        que=deque()
        path=set()
        def BFS(x,y):
            que.append((x,y))
            path.add((x,y))
            while que:
                x_s,y_s=que.popleft()
                if x_s+1<rows and board[x_s+1][y_s]=='O' and (x_s+1,y_s) not in path:
                    que.append((x_s+1,y_s))
                    path.add((x_s+1,y_s))
                if x_s-1>=0 and board[x_s-1][y_s]=='O' and (x_s-1,y_s) not in path:
                    que.append((x_s-1,y_s))
                    path.add((x_s-1,y_s))
                if y_s+1<cols and board[x_s][y_s+1]=='O' and (x_s,y_s+1) not in path:
                    que.append((x_s,y_s+1))
                    path.add((x_s,y_s+1))
                if y_s-1>=0 and board[x_s][y_s-1]=='O' and (x_s,y_s-1) not in path:
                    que.append((x_s,y_s-1))
                    path.add((x_s,y_s-1))
        for j in range(cols):
            if board[0][j]=='O' and (0,j) not in path:BFS(0,j)
        for j in range(cols):
            if board[rows-1][j]=='O' and (rows-1,j) not in path:BFS(rows-1,j)
        for i in range(1,rows-1):
            if board[i][0]=='O' and (i,0) not in path:BFS(i,0)
        for i in range(1,rows-1):
            if board[i][cols-1]=='O' and (i,cols-1) not in path:BFS(i,cols-1)
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if board[i][j]=='O' and (i,j) not in path:board[i][j]='X'
        return board
s=Solution()
matrix=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(s.solve(matrix))