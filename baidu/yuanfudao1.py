# N=int(input())
# courses=[]
# for i in range(N):
#     s,e=input().split()
#     courses.append([int(s),int(e)])
# def find_K(courses):
#     courses.sort(key=lambda x: x[1])
#     res=0
#     k=1
#     last=
#     for start,end in courses[1:]:
#         if last[1]<=start:
#             last[0]=start
#             last[1]=end
#             k=1
#         elif last[1]>end:
#             last[0]=start
#             last[1]=end
#             k+=1
#             res=max(res,k)
#         elif last[1]<=end:
#             la
#             res+=1
#     return res
# print(find_K(courses))



# N=int(input())
# courses=[]
# for i in range(N):
#     s,e=input().split()
#     courses.append([int(s),int(e)])
# def find_K(courses):
#     courses.sort(key=lambda x: x[1])
#     res=0
#     k=1
#     left=0
#     i=1
#     while i<len(courses):
#         start,end=courses[i][0],courses[i][1]
#         if courses[left][1]>start:
#             k+=1
#             res=max(res,k)
#             i+=1
#         else:
#             left+=1
#             k-=1
#     return res
# print(find_K(courses))


N=int(input())
courses=[]

arr=[]
exi=[]
for i in range(N):
    s,e=input().split()
    courses.append([int(s),int(e)])
    arr.append(int(s))
    exi.append(int(e))
def find_K(arr,exi):
    arr.sort()
    exi.sort()
    gin=1
    max_g=1
    time=arr[0]
    i=1
    j=0
    while i<len(arr) and j<len(exi):
        if arr[i]<exi[j]:
            gin+=1
            if gin>max_g:
                max_g=gin
                time=arr[i]
            i+=1
        else:
            gin-=1
            j+=1
    return max_g
print(find_K(arr,exi))
