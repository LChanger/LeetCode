def sqrt(num,p):
    if not num.isdigit():return "error num must be an digit"
    num=int(num)
    if num<0:return "error num must be an positive num"
    if num==0:return 0
    l=1
    r=num/2
    while l<r:
        mid=(l+r)/2
        cur=mid*mid
        if abs(cur-num)<p:return mid
        if cur<num:l=mid
        else:r=mid

num=input()
print(sqrt(num,0.0001))