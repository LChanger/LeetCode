#思路：记录所有的斜率对应的点数 用分数元组来表示斜率
class Solution:
    def maxPoints(self, points) -> int:
        if len(points)<3:return len(points)
        from collections import Counter,defaultdict
        #所有点统计
        points_dict=Counter(tuple(point) for point in points)
        #不重复点统计
        not_repeat_points=list(points_dict.keys())
        n=len(not_repeat_points)
        if n==1:return points_dict[not_repeat_points[0]]
        #求最大公约数
        def gcd(a,b):
            if b==0:return a
            while b!=0:
                c=a%b
                a=b
                b=c
            return a
        res=0
        for i in range(n-1):
            dot1_x,dot1_y=not_repeat_points[i]
            slope=defaultdict(int)
            truns_res=0
            for j in range(i+1,n):
                dot2_x,dot2_y=not_repeat_points[j]
                dy,dx=dot1_y-dot2_y,dot1_x-dot2_x
                #公约数
                g=gcd(dy,dx)
                if g!=0:
                    dx//=g
                    dy//=g
                slope["{}/{}".format(dx,dy)]+=points_dict[not_repeat_points[j]]
                truns_res=max(truns_res,slope["{}/{}".format(dx,dy)])
            res=max(res,truns_res+points_dict[not_repeat_points[i]])
        return res
points=[[1,1],[2,2],[3,3]]
print(Solution().maxPoints(points))