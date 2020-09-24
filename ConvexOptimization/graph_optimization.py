# from mpl_toolkits import mplot3d
import numpy as np
from sympy import *
import math
import matplotlib.pyplot as plt
# import mpl_toolkits.axisartist as axisartist

# 定义符号
x1, x2, t = symbols('x1, x2, t')
a,b=0,0
def func():
    return pow((a-x1), 2) + b * pow(x2-pow(x1,2),2)
def f_draw(x1,y1):
    return np.add(np.multiply(np.subtract(a,x1),np.subtract(a,x1)),b*np.subtract(y1,x1*x1)*np.subtract(y1,x1*x1))

def grad(data):
    # 求梯度向量,data=[data1, data2]
    f=func()
    grad_vec = [diff(f, x1), diff(f, x2)]  # 求偏导数,梯度向量
    grad = []
    for item in grad_vec:
        grad.append(item.subs(x1, data[0]).subs(x2, data[1]))
    return grad

def grad_len(grad):
    # 梯度向量的模长
    vec_len = math.sqrt(pow(grad[0], 2) + pow(grad[1], 2))
    return vec_len

def state_station(f):
    # 求得min(t)的驻点
    t_diff = diff(f)
    t_min = solve(t_diff)
    min_t=float("inf")
    res=1
    for i in range(len(t_min)):
        if t_min[i].args!=():continue
        y=f.subs(t, t_min[i])
        if min_t>y:
            res=t_min[i]
            min_t=y
    return res

# def binaryDivision(F,a,b):
#     T=0.5
#     k=0
#     while b-a>abs(A-B)*0.01:
#         mid=(a+b)/2
#         dx=derivative(F,mid, dx=1e-6)
#         if dx==0:
#             return k
#         elif dx>0:
#             b=mid
#         else:
#             a=mid
#         k+=1
#     return k,(b+a)/2

def main(X0, theta):
    f = func()
    grad_vec = grad(X0)
    grad_length = grad_len(grad_vec)  # 梯度向量的模长
    k = 0
    data_x = [X0[0]]
    data_y = [X0[1]]
    while grad_length > 2e-07:  # 迭代的终止条件
        k += 1
        p = -np.array(grad_vec)
        # 迭代
        X = np.array(X0) + t*p# t为步长
        t_func = f.subs(x1, X[0]).subs(x2, X[1])
        t_min = state_station(t_func)
        X0 = np.array(X0) + t_min*p
        grad_vec = grad(X0)
        grad_length = grad_len(grad_vec)
        print('grad_length', grad_length)
        print('坐标', X0[0], X0[1])
        data_x.append(X0[0])
        data_y.append(X0[1])

    print(k)
    return data_x,data_y
    #绘图

a = float(input("a是函数的参数："))
b = float(input("b是函数的参数："))
if __name__ == '__main__':
    ax = plt.axes(projection='3d')
    x = np.linspace(-1,1,200)
    y = np.linspace(-1,1,200)
    xData,yData = np.meshgrid(x,y)
    zData = f_draw(xData, yData)

    # fig = plt.figure()
    ax.plot_surface(xData, yData, zData,
                    rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.set_title('RosenBrock')

    # 绘制散点图
    # x_point = [] # 此处是x点的值
    # y_point = [] # 此处是y点的值
    x_point,y_point=main([0, 0], 0)
    z_point = []
    for i,j in zip(x_point,y_point):
        z_point.append(pow((a-i), 2) + b * pow(j-pow(i,2),2))  
    ax.plot3D(np.array(x_point), np.array(y_point), np.array(z_point), 'red')
    plt.show()