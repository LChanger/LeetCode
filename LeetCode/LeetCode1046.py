import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        neg_stones=[]
        for digit in stones:
            heapq.heappush(neg_stones,-digit)
        while len(neg_stones)>1:
            x=-heapq.heappop(neg_stones)
            y=-heapq.heappop(neg_stones)
            if x>y:
                heapq.heappush(neg_stones,y-x)
        return -neg_stones[0] if neg_stones else 0
stones=[2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))