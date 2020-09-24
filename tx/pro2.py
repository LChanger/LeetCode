n=int(input())
xishu=list(map(int,input().split()))
# # import numpy as np
# # print(np.roots(xishu))
# # jie=np.roots(xishu)
# pre=None
# for x in jie:
#     if pre and pre==x:continue
#     pre=x
#     if not np.isreal(x):continue
#     print(round(np.real(x),2))

def get_daoshu(nums,n,x):
    ant=0
    for i in range(len(nums)):
        if x==0:
            if n-1-i==1:
                ant+=nums[i]
            continue
        ant+=nums[i]*x**(n-1-i)
    return ant

def get_sum(nums,n,x):
    ant=0
    for i in range(len(nums)):
        ant+=nums[i]*x**(n-i)
    return ant

def round_up(value):
    return round(value*100)/100.0

from decimal import Decimal
def newton(xushu,n):
    x0=0
    e=1e-4
    nums=[]
    cishu=n
    for i in range(len(xishu)):
        nums.append(xishu[i]*(n-i))
    xn=x0-get_sum(xishu,n,x0)/get_daoshu(nums,n,x0)
    
    while abs(xn-x0)>e:
        x0=xn
        xn=x0-get_sum(xishu,n,x0)/get_daoshu(nums,n,x0)
    return xn
# print(round(round_up(newton(xishu,n)),4))
print(round(Context(prec=3,rounding=ROUND_HALF_UP).create_decimal(newton(xishu,n)),4))