from scipy.misc import derivative
F=lambda x: x*x/2-x
A,B=0,1000
def goldDivision(F,a,b):
    T=0.618
    k=0
    while b-a>abs(A-B)*0.01:
        c1=a+(1-T)*(b-a)
        c2=b-(1-T)*(b-a)
        Fc1=F(c1)
        Fc2=F(c2)
        print("k:{:0.3f},a:{:0.3f},c1:{:0.3f},c2:{:0.3f},b:{:0.3f},Fc1:{:0.3f},Fc2:{:0.3f}".format(k,a,c1,c2,b,Fc1,Fc2))
        if Fc1-Fc2>0:
            a=c1
        else:
            b=c2
        k+=1
    return k,(b+a)/2

def fibonacciDivision(F,a,b):
    def fabList(Fmax):
        a,b=0,1
        Fablist = [a,b]  # 返回一个列表
        while Fablist[-1]< Fmax:
            a,b = b,a+b
            Fablist.append(b)
        a,b = b,a+b
        Fablist.append(b)
        return Fablist
    fab=fabList(100)
    k=len(fab)-1
    if k<4:return 0,(a+b)/2
    c1=a+fab[k-2]/fab[k]*(b-a)
    c2=a+fab[k-1]/fab[k]*(b-a)
    while k>=3:
        Fc1=F(c1)
        Fc2=F(c2)
        if Fc1-Fc2>0:
            a=c1
            c1=c2
            c2=a+fab[k-2]/fab[k-1]*(b-a)
        elif Fc1<Fc2:
            b=c2
            c2=c1
            c1=a+fab[k-3]/fab[k-1]*(b-a)
        else:
            a=c1
            b=c2
            c1=a+fab[k-3]/fab[k-1]*(b-a)
            c2=a+fab[k-2]/fab[k-1]*(b-a)
        print("k:{:0.3f},a:{:0.3f},c1:{:0.3f},c2:{:0.3f},b:{:0.3f},Fc1:{:0.3f},Fc2:{:0.3f}".format(k,a,c1,c2,b,Fc1,Fc2))
        k-=1
    return len(fab)-1-k,(b+a)/2

def binaryDivision(F,a,b):
    T=0.5
    k=0
    while b-a>abs(A-B)*0.01:
        mid=(a+b)/2
        dx=derivative(F,mid, dx=1e-6)
        print("k:{:0.3f},a:{:0.3f},b:{:0.3f},dx:{:0.3f}".format(k,a,b,mid,dx))
        if dx==0:
            return k
        elif dx>0:
            b=mid
        else:
            a=mid
        k+=1
    return k,(b+a)/2

k,v=goldDivision(F,A,B)
print("黄金分割法所需次数为：{:.0f},答案为：{:0.3f}".format(k,v))
k,v=fibonacciDivision(F,A,B)
print("fibonacci分割法所需次数为：{:.0f},答案为：{:0.3f}".format(k,v))
k,v=binaryDivision(F,A,B)
print("二分法所需次数为：{:.0f},答案为：{:0.3f}".format(k,v))