class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for layer in range(int(n/2)):
            for j in range(layer,n-layer-1):
                x,y=layer,j
                temp=matrix[x][y]
                for p in range(4):
                    matrix[y][n - 1 - x],temp=temp,matrix[y][n-1-x]
                    x,y=y,n-1-x
                    print('x:',x,'y',y)
                print(matrix)
        return matrix

    # 坐标对应关系为 （x,y）旋转后变为（y,n-1-x）  然后 [0][0]向中间递进，相当于先旋转外层，再旋转内层，逐层旋转
c=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
t=Solution()
print (t.rotate(c))