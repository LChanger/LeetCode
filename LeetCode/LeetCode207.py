#思路：拓扑排序
#T:O(nlogn))
#S:O(n)
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if not prerequisites:return True
        #入度字典
        Penetration={}
        Adjacency=[[] for i in range(numCourses)]
        for nc1,nc2 in prerequisites:
            Penetration[nc1]=Penetration.get(nc1,0)+1
            Adjacency[nc2].append(nc1)
        from collections import deque
        queue=deque(set([i for i in range(numCourses)])-set(Penetration.keys()))
        while queue:
            node=queue.popleft()
            for n in Adjacency[node]:
                Penetration[n]-=1
                if Penetration[n]==0:queue.append(n)
            numCourses-=1
        return True if numCourses==0 else False
numCourses,prerequisites=2,[[1,0],[0,1]]
s=Solution()
print(s.canFinish(numCourses,prerequisites))
