s=input()
char={}
i=j=0
while i<len(s):
    j=i
    while j<len(s) and s[j]==s[i]:j+=1
    if j-i>=3:
        s=s[:i]+s[j:]
        i=max(i-2,0)
    else:
        i+=1
print(s)
