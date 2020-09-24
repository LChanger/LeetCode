N=input()
addmax={
    0:8,
    1:7,
    3:9,
    5:9,
    6:8,
    9:8
}
rmmax={
    7:1,
    8:9,
    9:5
}
changemax={
    0:9,
    2:3,
    3:5,
    5:3,
    6:9,
    9:6
}
def getMax(N):
    if len(N)==1:
        return changemax.get(int(N),-1)
    res=int(N)
    for i in range(len(N)):
        cnum=changemax.get(int(N[i]),-1)
        anum=addmax.get(int(N[i]),-1)
        rnum=rmmax.get(int(N[i]),-1)
        if cnum>anum and cnum>rnum:
            return max(res,int(N[:i]+str(cnum)+N[i+1:]))
        if cnum<=anum and anum!=-1:
            for j in range(i+1,len(N)):
                if int(N[j]) in rmmax:
                    jnum=rmmax[int(N[j])]
                    res=max(res,int(N[:i]+str(anum)+N[i+1:j]+str(jnum)+N[j+1:]))
                    break
        if cnum<=rnum and rnum!=-1:
            for j in range(i+1,len(N)):
                if int(N[j]) in addmax:
                    jnum=addmax[int(N[j])]
                    res=max(res,int(N[:i]+str(anum)+N[i+1:j]+str(jnum)+N[j+1:]))
                    break
        if res>int(N):return res
    if res==int(N):return -1
    return res
print(getMax(N))