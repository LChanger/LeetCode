class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        indexs=defaultdict(list)
        for i in range(len(ring)):
            indexs[ring[i]].append(i)
        def count_distance(p_ring,t_key):
            #p_ring现在指针停在的位置，t_key是要转到的对应的字符
            distance=len(ring)-1
            next_p=p_ring
            for i in indexs[t_key]:
                next_d=min(abs(p_ring-i),len(ring)-abs(p_ring-i))
                if next_d<distance:
                    distance=next_d
                    next_p=i
            return distance,next_p
        p_ring=0
        distance=0
        for i in range(len(key)):
            d,p=count_distance(p_ring,key[i])
            distance+=d+1
            p_ring=p
        return distance
ring = "godding"
key = "gd"
print(Solution().findRotateSteps(ring,key))