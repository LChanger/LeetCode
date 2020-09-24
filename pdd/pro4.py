ch=[]
for i in range(6):
    temp=[]
    for c in input():
        temp.append(c)
    ch.append(temp)
# print(ch)
def get_types():
    res=0
    for i in range(6):
        j=0
        while j<6:
            if ch[i][j]=='#':
                left=-1
                upper=-1
                if i>0 and ch[i-1][j]<='6' and ch[i-1][j]>48:
                    left=ch[i-1][j]-'0'
                if j>0 and ch[i][j-1]<='6' and ch[i][j-1]>'0':
                    upper=ch[i][j-1]-48
                for k in range(6,0,-1):
                    if upper==k or left==k:
                        continue
                    ch[i][j]=str(k+48)
                    cur=get_types()
                    if cur==0:res+=1
                    else:res+=cur
                    res=res%1000000009
                ch[i][j]='#'
                break
            j+=1
        if j<6:break
    return res%1000000009
print(get_types())
