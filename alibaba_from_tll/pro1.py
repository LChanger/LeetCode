T=int(input())
for i in range(T):
    NM=input().split()
    N=int(NM[0])
    M=int(NM[1])
    x=N//2+N%2#奇数个数
    y=M//2+M%2
    child=x*(M-y)+(N-x)*y
    parent=N*M
    if parent%child==0:
        print("1/"+str(parent//child))
        continue
    for j in range(2,child):
        if child%j==0 and parent%j==0:
            child//=j
            parent//=j
    print(str(child)+"/"+str(parent))


# T=int(input())
# for i in range(T):
#     NM=input().split()
#     N=int(NM[0])
#     M=int(NM[1])
#     if N%2==0 and M%2==0:
#         print("1/2")
#     elif N%2==1 and M%2==1:
#         child=M*N-1
#         parent=2*N*M
#         if child==0:
#             print("0/1")
#             continue
#         if parent%child==0:
#             print("1/"+str(parent//child))
#             continue
#         for j in range(2,child+1):
#             if child%j==0 and parent%j==0:
#                 child//=j
#                 parent//=j
#         print(str(child)+"/"+str(parent))
#     else:
#         print("1/2")
