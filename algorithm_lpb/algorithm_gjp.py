from tkinter import *
import time

# 初始化地图
colors = ['white', 'yellow', 'blue', 'black', 'red', 'green']
#真实数据

L = 40
W = 20
M = [[0 for _ in range(W)] for _ in range(L)]
M[24][0]=1
M[25][0]=1
M[26][0]=1
M[27][0]=1
M[28][0]=1
M[29][0]=1
M[30][0]=1
M[31][0]=1
M[32][0]=1
M[33][0]=1
M[34][0]=1
M[35][0]=1
M[36][0]=1
M[37][0]=1
M[38][0]=1
M[39][0]=1
M[25][1]=1
M[26][1]=1
M[27][1]=1
M[28][1]=1
M[29][1]=1
M[30][1]=1
M[31][1]=1
M[32][1]=1
M[33][1]=1
M[34][1]=1
M[35][1]=1
M[36][1]=1
M[37][1]=1
M[38][1]=1
M[39][1]=1
M[26][2]=1
M[27][2]=1
M[28][2]=1
M[29][2]=1
M[30][2]=1
M[31][2]=1
M[32][2]=1
M[33][2]=1
M[34][2]=1
M[35][2]=1
M[36][2]=1
M[37][2]=1
M[38][2]=1
M[39][2]=1
M[26][3]=1
M[27][3]=1
M[28][3]=1
M[29][3]=1
M[30][3]=1
M[31][3]=1
M[32][3]=1
M[33][3]=1
M[34][3]=1
M[35][3]=1
M[36][3]=1
M[26][4]=1
M[27][4]=1
M[28][4]=1
M[29][4]=1
M[30][4]=1
M[31][4]=1
M[32][4]=1
M[33][4]=1
M[34][4]=1
M[35][4]=1
M[27][5]=1
M[28][5]=1
M[29][5]=1
M[30][5]=1
M[31][5]=1
M[32][5]=1
M[27][6]=1
M[28][6]=1
M[29][6]=1
M[30][6]=1
M[31][6]=1
M[32][6]=1
M[29][7]=1
M[30][7]=1
M[31][7]=1
M[32][7]=1

M[34][1]=2
M[33][2]=2
M[32][3]=2
M[33][4]=2
M[34][5]=2
M[33][5]=2
M[34][6]=2
M[33][6]=2
M[33][7]=2
M[34][7]=2
M[35][7]=2
M[32][8]=2
M[33][8]=2
M[34][8]=2
M[35][8]=2
M[32][9]=2
M[33][9]=2
M[34][9]=2
M[32][10]=2
M[33][10]=2
M[35][10]=2
M[36][10]=2
M[32][11]=2
M[34][11]=2
M[35][11]=2
M[33][12]=2
M[34][12]=2
M[32][13]=2
M[33][13]=2
M[34][13]=2
M[32][14]=2
M[33][14]=2
M[34][14]=2
M[31][15]=2
M[32][15]=2
M[33][15]=2
M[31][16]=2
M[32][16]=2
M[33][16]=2
M[30][17]=2
M[31][17]=2
M[32][17]=2
M[29][18]=2
M[30][18]=2
M[31][18]=2
M[28][19]=2
M[29][19]=2
M[30][19]=2

M[3][0] = 3
M[7][0] = 3
M[12][0] = 3
M[7][1] = 3
M[12][1] = 3
M[0][2] = 3
M[1][2] = 3
M[2][2] = 3
M[3][2] = 3
M[4][2] = 3
M[5][2] = 3
M[7][2] = 3
M[8][2] = 3
M[9][2] = 3
M[10][2] = 3
M[12][2] = 3
M[8][3] = 3
M[12][3] = 3
M[12][4] = 3
M[7][5] = 3
M[8][5] = 3
M[12][5] = 3
M[2][6] = 3
M[3][6] = 3
M[4][6] = 3
M[5][6] = 3
M[6][6] = 3
M[7][6] = 3
M[12][6] = 3
M[2][7] = 3
M[5][7] = 3
M[7][7] = 3
M[12][7] = 3
M[36][7] = 3
M[5][8] = 3
M[5][9] = 3
M[7][9] = 3
M[36][9] = 3
M[2][10] = 3
M[5][10] = 3
M[7][10] = 3
M[8][10] = 3
M[19][10] = 3
M[20][10] = 3
M[21][10] = 3
M[28][10] = 3
M[2][11] = 3
M[3][11] = 3
M[4][11] = 3
M[5][11] = 3
M[8][11] = 3
M[19][11] = 3
M[20][11] = 3
M[21][11] = 3
M[31][11] = 3
M[3][12] = 3
M[8][12] = 3
M[12][12] = 3
M[19][12] = 3
M[20][12] = 3
M[21][12] = 3
M[3][13] = 3
M[8][13] = 3
M[9][13] = 3
M[11][13] = 3
M[12][13] = 3
M[31][13] = 3
M[3][14] = 3
M[8][14] = 3
M[12][14] = 3
M[3][15] = 3
M[4][15] = 3
M[5][15] = 3
M[6][15] = 3
M[7][15] = 3
M[8][15] = 3
M[12][15] = 3
M[24][15] = 3
M[25][15] = 3
M[3][16] = 3
M[12][16] = 3
M[24][16] = 3
M[25][16] = 3
M[7][17] = 3
M[12][17] = 3
M[3][18] = 3
M[7][18] = 3
M[12][18] = 3
M[3][19] = 3
M[7][19] = 3
M[12][19] = 3

s = [4,10]
t = [35,0]



# 测试数据
# L = 13
# W = 10
# M = [[0 for _ in range(W)] for _ in range(L)]
# M[3][1]=3
# M[3][2]=3
# M[4][3]=3
# M[4][4]=3
# M[4][5]=3
# M[5][5]=3
# M[5][6]=3
# M[5][7]=3
# s = [1,4]
# t = [10,5]
class Node:
    def __init__(self,x,y,t):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 1.414*min(abs(t[0]-x),abs(t[1]-y))+abs(abs(t[0]-x)-abs(t[1]-y))
        self.father = None

def topography(M,x,y):
    result = 0
    if M[x][y] == 0:
        result = 0
    elif M[x][y] == 1:
        result = 4
    elif M[x][y] == 2:
        result = 2
    return result
def A(M,s,t):
    lenth = len(M)
    width = len(M[0])
    close = [[False for _ in range(width)] for _ in range(lenth)]
    node = Node(s[0],s[1],t)
    node.g = 0
    nodes = [node]
    close[s[0]][s[1]] = True
    best_index = 0
    while nodes[best_index].h:
        # print('==========')
        # for nn in nodes:
        #     print(nn.x,nn.y,nn.g,nn.h)
        # print('--------------')
        best = nodes[best_index]
        # print(best.x, best.y)
        for i in range(1,9):
            tx = 0
            ty = 0
            tc = 1
            if i == 1 or i == 4 or i == 6:
                tx = -1
            if i == 3 or i == 5 or i == 8:
                tx = 1
            if i == 1 or i == 2 or i == 3:
                ty = -1
            if i == 6 or i == 7 or i == 8:
                ty = 1
            if i == 1 or i == 3 or i == 6 or i == 8:
                tc = 1.414
            newx = best.x+tx
            newy = best.y+ty
            if newx<0 or newx>=lenth or newy<0 or newy>=width or M[newx][newy] == 3:
                continue
            if close[newx][newy]:
                for i in range(len(nodes)):
                    if nodes[i].x == newx and nodes[i].y==newy and nodes[i].g > best.g + tc + topography(M, nodes[i].x, nodes[i].y):
                        nodes[i].father = best
                        nodes[i].g = best.g + tc + topography(M, nodes[i].x, nodes[i].y)
            else:
                n1 = Node(newx,newy,t)
                n1.father = best
                n1.g = best.g + tc + topography(M,n1.x,n1.y)
                nodes.append(n1)
                close[newx][newy] = True

        nodes.pop(best_index)
        best_index = 0
        for i in range(len(nodes)):
            if nodes[best_index].g+nodes[best_index].h > nodes[i].g+nodes[i].h:
                best_index = i
    result = nodes[best_index]
    while result:
        M[result.x][result.y] = 4
        result = result.father

def drawboard(board, colors, startx=100, starty=100, cellwidth=20):
    width = 2 * startx + len(board) * cellwidth
    height = 2 * starty + len(board[0]) * cellwidth
    canvas.config(width=width, height=height)
    for i in range(len(board)):
        for j in range(len(board[0])):
            index = board[i][j]
            color = colors[index]
            cellx = startx + i * 20
            celly = starty + j * 20
            canvas.create_rectangle(cellx, celly, cellx + cellwidth, celly + cellwidth,
                                    fill=color, outline="black")
    canvas.update()
start = time.process_time()
A(M,s,t)
M[s[0]][s[1]]=5
M[t[0]][t[1]]=5
timeuesd = (time.process_time()-start)
print('Time used:', timeuesd)
root = Tk()
canvas = Canvas(root, bg="white")
canvas.pack()
drawboard(M, colors)
root.mainloop()