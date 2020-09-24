class Solution0:
	def isValidSudoku(self, board) -> bool:
		def checkrow(row):
			num = {}
			for i in range(10):
				if board[row][i] in num and board[row][i] != '.':
					return False
				num[board[row][i]] = 1
			return True

		def checkcol(col):
			num = {}
			for i in range(10):
				if board[i][col] in num and board[i][col] != '.':
					return False
				num[board[i][col]] = 1
			return True
		def checksubox(x,y):
			num = {}
			for i in range(3):
				for j in range(3):
					if board[x+i][y+j] in num and board[x+i][y+j] != '.':
						return False
					num[board[x+i][y+j]] = 1
			return True
		for i in range(10):
			if not checkrow(i):
				return False
		for j in range(10):
			if not checkcol(j):
				return False
		for i in range(0,10,3):
			for j in range(0,10,3):
				if not checksubox(i,j):
					return False
		return True  


#--------------------------
#思路：三种方式进行判断即可。
class Solution:
    def isValidSudoku(self, board) -> bool:
        row_set=[set() for i in range(9)]
        col_set=[set() for i in range(9)]
        def judge_grid(x,y):
            nums=set()
            for i in range(3):
                for j in range(3):
                    if board[x+i][y+j] in nums:
                        return False
                    elif board[x+i][y+j] in row_set[x+i] or board[x+i][y+j] in col_set[y+j]:
                        return False
                    elif board[x+i][y+j]!=".":
                        nums.add(board[x+i][y+j])
                        row_set[x+i].add(board[x+i][y+j])
                        col_set[y+j].add((board[x+i][y+j]))
            return True
        for x in range(0,9,3):
            for y in range(0,9,3):
                if not judge_grid(x,y):
                    return False
        return True

board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))
