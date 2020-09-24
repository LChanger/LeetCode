# -*- coding:utf-8 -*-
"""
运行时间：39ms
占用内存：5624k
"""
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        #BFS问题
        def reachable(x,y):
            sum=0
            for i in str(x):
                sum+=int(i)
                if sum>threshold:return False
            for j in str(y):
                sum+=int(j)
                if sum>threshold:return False
            return True
        matrix=[[False for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                matrix[i][j]=reachable(i,j)
        from collections import deque
        que=deque()
        if not matrix[0][0]:return 0
        que.append((0,0))
        sum=1
        matrix[0][0]=False
        while que:
            top=que.popleft()
            if top[0]+1<rows and matrix[top[0]+1][top[1]]:
                que.append((top[0]+1,top[1]))
                matrix[top[0]+1][top[1]]=False
                sum+=1
            if top[0]-1>=0 and matrix[top[0]-1][top[1]]:
                que.append((top[0]-1,top[1]))
                matrix[top[0]-1][top[1]]=False
                sum+=1
            if top[1]+1<cols and matrix[top[0]][top[1]+1]:
                que.append((top[0],top[1]+1))
                matrix[top[0]][top[1]+1]=False
                sum+=1
            if top[1]-1>=0 and matrix[top[0]][top[1]-1]:
                que.append((top[0],top[1]-1))
                matrix[top[0]][top[1]-1]=False
                sum+=1
        return sum
'''
运行时间：25ms
占用内存：5720k
'''
class Solution1:
    def movingCount(self, threshold, rows, cols):
        # write code here
        #BFS问题
        def reachable(x,y):
            sum=0
            for i in str(x):
                sum+=int(i)
                if sum>threshold:return False
            for j in str(y):
                sum+=int(j)
                if sum>threshold:return False
            return True
        matrix=[[True for j in range(cols)] for i in range(rows)]
        from collections import deque
        que=deque()
        #modify
        if not reachable(0,0):return 0
        que.append((0,0))
        sum=1
        matrix[0][0]=False
        while que:
            top=que.popleft()
            if top[0]+1<rows and matrix[top[0]+1][top[1]] and reachable(top[0]+1,top[1]):
                que.append((top[0]+1,top[1]))
                matrix[top[0]+1][top[1]]=False
                sum+=1
            if top[0]-1>=0 and matrix[top[0]-1][top[1]] and reachable(top[0]-1,top[1]):
                que.append((top[0]-1,top[1]))
                matrix[top[0]-1][top[1]]=False
                sum+=1
            if top[1]+1<cols and matrix[top[0]][top[1]+1] and reachable(top[0],top[1]+1):
                que.append((top[0],top[1]+1))
                matrix[top[0]][top[1]+1]=False
                sum+=1
            if top[1]-1>=0 and matrix[top[0]][top[1]-1] and reachable(top[0],top[1]-1):
                que.append((top[0],top[1]-1))
                matrix[top[0]][top[1]-1]=False
                sum+=1
        return sum
s=Solution()
print(s.movingCount(5,10,10))