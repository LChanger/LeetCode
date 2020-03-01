# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m=len(matrix)
        if m==0:return []
        n=len(matrix[0])
        path=[[True for j in range(n)] for i in range(m)]
        i,j=0,0#为已经访问过的点
        step=1
        res=[matrix[i][j]]
        path[i][j]=False
        while step<m*n:
            while j<n-1 and path[i][j+1]:
                j+=1
                res.append(matrix[i][j])
                path[i][j]=False
                step+=1
            while i<m-1 and path[i+1][j]:
                i+=1
                res.append(matrix[i][j])
                path[i][j]=False
                step+=1
            while j>0 and path[i][j-1]:
                j-=1
                res.append(matrix[i][j])
                path[i][j]=False
                step+=1
            while i>0 and path[i-1][j]:
                i-=1
                res.append(matrix[i][j])
                path[i][j]=False
                step+=1
        return res
t=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s=Solution()
print (s.printMatrix(t))   