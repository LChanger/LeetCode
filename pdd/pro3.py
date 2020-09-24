nmt=list(map(int,input().split()))
n,m,t=nmt[0],nmt[1],nmt[2]
lunch=[]
for i in range(n):
    lunch.append(list(map(int,input().split())))
dinner=[]
for i in range(m):
    dinner.append(list(map(int,input().split())))

def get_hot(lunch,dinner):
    lunch.sort(key=lambda x: x[1])
    dinner.sort(key=lambda x: x[1])
    res=10**6
    for i in range(n):
        if lunch[i][1]>=t:
            res=min(res,lunch[i][0])
            # continue
        for j in range(m):
            if dinner[j][1]>=t:
                res=min(res,dinner[j][0])
                continue
            if dinner[j][1]+lunch[i][1]>=t:
                res=min(res,dinner[j][0]+lunch[i][0])
    return res
print(get_hot(lunch,dinner))