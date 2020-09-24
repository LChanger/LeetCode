# def binarySearch(a,i,j,target):
#     if i==j:
#         if i<len(a) and i>=0 and a[i]<=target:
#             return a[i]
#         elif i==len(a) and i>0:
#             return a[i-1]
#         return 0
#     mid=(i+j)//2
#     if target<a[mid]:
#         mid=binarySearch(a,i,mid,target)
#         if mid<=target:return mid
#         return 0
#     elif target==a[mid]:
#         return target
#     else:
#         mid=binarySearch(a,mid+1,j,target)
#         if mid>target or mid==0:
#             return a[mid]
#         return mid

def binarySearch(a,start,end,target):
    if not a:return 0
    while start<end:
        mid=(start+end+1)//2
        if a[mid]==target:return a[mid]
        elif a[mid]<target:start=mid
        else:end=mid-1
    return a[start]
nm=input().split()
n,m=int(nm[0]),int(nm[1])
a=list(map(lambda x: int(x),input().split()))
b=list(map(lambda x: int(x),input().split()))
a.sort()
sum=0

for i in range(len(b)):
    sub=binarySearch(a,0,len(a)-1,b[i])
    if sub<=b[i]:sum+=b[i]-sub
    else:sum+=b[i]
print(sum)