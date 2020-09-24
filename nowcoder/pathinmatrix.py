class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        flag=[[True for i in range(cols)] for j in range(rows)]
        def backTrack(x,y,index):
            if not flag[x][y] or matrix[x][y]!=path[index]:return False
            flag[x][y]=False
            if index==len(path)-1:return True
            if y+1<cols and backTrack(x,y+1,index+1):return True
            if y-1>=0 and backTrack(x,y-1,index+1):return True
            if x+1<rows and backTrack(x+1,y,index+1):return True
            if x-1>=0 and backTrack(x-1,y,index+1):return True
            flag[x][y]=True
            return False
        for i in range(rows):
            for j in range(cols):
                if backTrack(i,j,0):return True
        return False
s=Solution()
matrix=[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
path="ABCCED"
row=len(matrix)
cols=len(matrix[0])
print(s.hasPath(matrix,row,cols,path))