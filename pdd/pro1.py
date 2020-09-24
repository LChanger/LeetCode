KN=input().split()
K=int(KN[0])
N=int(KN[1])
dots=list(map(int,input().split()))
def find_index_times(K,dots):
    index=K
    times=0
    for i in range(len(dots)):
        index-=dots[i]
        if index==0:
            print("paradox")
            return 
        if index<0:
            times+=1
            index=-index
    print(index,times)
find_index_times(K,dots)