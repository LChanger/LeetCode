#思路：最短路径算法
class Solution:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        from collections import defaultdict
        #init graph
        from queue import PriorityQueue
        penetration=defaultdict(list)
        for u,v,w in times:
            penetration[u].append((w,v))
        #Dijkstra
        adjacency=PriorityQueue()
        adjacency.put((0,K))
        dist={}#记录最优路径
        while not adjacency.empty():
            w,nearest=adjacency.get()
            if nearest in dist:continue#已经记录下了最优路径
            dist[nearest]=w
            for nw,nv in penetration.get(nearest,[]):
                if nv not in dist:
                    adjacency.put((w+nw,nv))
        return max(dist.values()) if len(dist)==N else -1
times=[[2,1,1],[2,3,1],[3,4,1]]
N=4
K=2
s=Solution()
print(s.networkDelayTime(times,N,K))