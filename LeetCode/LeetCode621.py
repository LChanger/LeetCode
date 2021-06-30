import collections,heapq
class Solution0:
    def leastInterval(self, tasks, n: int) -> int:
        #贪心算法
        if n==0:return len(tasks)
        task_cnt=collections.Counter(tasks)
        # queue=[]
        # for x in task_cnt.values():
        #     queue.append(-x)
        queue=sorted(task_cnt.values(),reverse=True)
        queue=list(map(lambda x: -x,queue))
        costs=0
        waite=0
        while queue:
            i=0
            waite=0
            temp=[]
            while queue and waite<n+1:
                x=-queue[0]
                x-=1
                if x!=0:
                    temp.append(x)
                queue.pop(0)
                waite+=1
                costs+=1
            for x in temp:
                heapq.heappush(queue,-x)
            if waite<n+1 and queue:
                costs+=n+1-waite
        return costs

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        #贪心算法
        if n==0:return len(tasks)
        task_cnt=collections.Counter(tasks)
        # queue=[]
        # for x in task_cnt.values():
        #     queue.append(-x)
        queue=sorted(task_cnt.values(),reverse=True)
        # queue=list(map(lambda x: -x,queue))
        costs=0
        waite=0
        while queue:
            i=0
            waite=0
            while i<len(queue) and waite<n+1:
                queue[i]-=1
                if queue[i]==0:
                    queue.pop(i)
                else:
                    i+=1
                waite+=1
                costs+=1
            if waite<n+1 and queue:
                costs+=n+1-waite
            queue.sort(reverse=True)
        return costs
tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2
print(Solution().leastInterval(tasks,n))