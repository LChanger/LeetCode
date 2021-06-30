class Solution:
    def islandPerimeter(self, grid) -> int:
        if not grid:return 0
        m=len(grid)
        n=len(grid[0])
        girth=0
        from collections import deque
        que=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    que.append((i,j))
                    visited=set()
                    visited.add((i,j))
                    while que:
                        x,y=que.popleft()
                        girth+=4
                        if y+1<n and grid[x][y+1]==1:
                            girth-=1
                            if (x,y+1) not in visited:
                                que.append((x,y+1))
                                visited.add((x,y+1))
                        if x+1<m and grid[x+1][y]==1:
                            girth-=1
                            if (x+1,y) not in visited:
                                que.append((x+1,y))
                                visited.add((x+1,y))
                        if y-1>=0 and grid[x][y-1]==1:
                            girth-=1
                            if (x,y-1) not in visited:
                                que.append((x,y-1))
                                visited.add((x,y-1))
                        if x-1>=0 and grid[x-1][y]==1:
                            girth-=1
                            if (x-1,y) not in visited:
                                que.append((x-1,y))
                                visited.add((x-1,y))
                    return girth
        return girth
grid=[[1,0,1],[1,1,1]]
print(Solution().islandPerimeter(grid))