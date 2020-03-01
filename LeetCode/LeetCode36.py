class Solution:
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
