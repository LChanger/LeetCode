nums=list(map(int,input().split()))
N,M,L=nums[0],nums[1],nums[2]
board=[]
for i in range(N):
    board.append([])
    for j in range(M):
        board[-1].append(list(map(int,input().split())))

value=0
for i in range(N):
    for j in range(M):
        for k in range(L):
            if board[i][j][k]>0:
                value+=board[i][j][k]
print(N*M,value)