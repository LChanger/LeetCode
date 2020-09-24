N=int(input())
dots=[]
for i in range(N):
    dots.append(list(map(int,input().split())))

def R(nums):
    shang=nums[0]
    xia=nums[1]
    zuo=nums[2]
    you=nums[3]
    qian=nums[4]
    hou=nums[5]
    # 前后45不变
    s=you
    z=shang
    x=zuo
    y=xia
    nums[0]=s
    nums[2]=z
    nums[1]=x
    nums[3]=y
def U(nums):
    shang=nums[0]
    xia=nums[1]
    zuo=nums[2]
    you=nums[3]
    qian=nums[4]
    hou=nums[5]
    # 左右23不变
    s=qian
    q=xia
    x=hou
    h=shang
    nums[0]=s
    nums[4]=q
    nums[1]=x
    nums[5]=h
def Q(nums):
    shang=nums[0]
    xia=nums[1]
    zuo=nums[2]
    you=nums[3]
    qian=nums[4]
    hou=nums[5]
    # 上下01不变
    q=zuo
    y=qian
    h=you
    z=hou
    nums[4]=q
    nums[3]=y
    nums[5]=h
    nums[2]=z





def judge_type(nums):
    #把1放到上面
    if nums[0]!=1:
        index1=nums.index(1)
        #下边
        if index1==1:
            U(nums)
            U(nums)
        #在左边
        elif index1==2:
            R(nums)
            R(nums)
            R(nums)
        #在右边
        elif index1==3:
            R(nums)
        #在前边
        elif index1==4:
            U(nums)
        #在后边
        elif index1==5:
            U(nums)
            U(nums)
            U(nums)
    #最小的应该在左边
    min_index=2
    for i in range(3,6):
        if nums[min_index]>nums[i]:
            min_index=i
    if min_index==3:
        Q(nums)
        Q(nums)
    elif min_index==4:
        Q(nums)
        Q(nums)
        Q(nums)
    elif min_index==5:
        Q(nums)
    return nums


def find_types():
    tpyes={}
    for nums in dots:
        temp=judge_type(nums)
        tp=""
        for n in temp:
            tp+=str(n)
        tpyes[tp]=tpyes.get(tp,0)+1
    print(len(tpyes))
    res=sorted(tpyes.values(),reverse=True)
    for r in res:
        print(r,end=" ")
    
find_types()