# nk=input().split()
# k,n=int(nk[0]),int(nk[1])
# def fibonacci(k,n):
#     if k<1:return 0
#     if k>n:return 1
#     def func(k,n):
#         sum=0
#         if n<k-1:return 1
#         if n==k-1:return 1
#         for i in range(1,k+1):
#             sum+=func(k,n-i)%397
#         return sum
#     return func(k,n)
# print(fibonacci(k,n))




nk=input().split()
k,n=int(nk[0]),int(nk[1])
from collections import deque
q=deque()
for i in range(k):
    q.append(1)
sumq=k%397
for i in range(k,n+1):
    q.append(sumq)
    sumq=(sumq-q.popleft()+q[-1]%397)%397
print(q[-1])