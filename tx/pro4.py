T=int(input())
for i in range(T):
    n=int(input())
    array=[]
    for x in range(n):
        array.append(list(map(int,input().split())))
    cache={}
    flag=False
    for nums in array:
        zhuanhuan=tuple(sorted(nums))
        if zhuanhuan in cache:
            print("YES")
            flag=True
            break
        cache[zhuanhuan]=1
    if not flag:print("NO")

