class Solution:
    def spiralOrder(self, matrix):
        x_le=len(matrix)
        if x_le==0:return []
        y_le=len(matrix[0])
        res=[]
        path=[[True for i in range(y_le)] for j in range(x_le)]
        x,y=0,0
        direct=[
            [0,1],#向右走
            [1,0],#向下走
            [0,-1],#向左走
            [-1,0]#向上走
        ]
        d=0
        times=0#碰壁次数
        res.append(matrix[x][y])
        path[x][y]=False
        while times<2:
            next_x,next_y=x+direct[d][0],y+direct[d][1]
            if next_x<x_le and next_y<y_le and path[next_x][next_y]==True:
                x,y=next_x,next_y
                res.append(matrix[x][y])
                path[x][y]=False
                times=0
            else:
                d=(d+1)%4
                times+=1
        return res
n=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
t=Solution()
print (t.spiralOrder(n))