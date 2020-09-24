#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

// 最速下降算法

struct Grad{
 double x1; // 表示两个方向
 double x2;
 Grad(double x = 0, double y = 0) :x1(x), x2(y){}
};

struct Point{
 double x1;
 double x2;
 Point(double x = 0, double y = 0) :x1(x), x2(y){}
};

class Rosenbrock{
public:
 // 得到某个点的梯度
 void getGrad(const Point& p, const double& a, const double& b, Grad* & result){
  //Grad* result = new Grad(); // 堆中分配的都是指针
  result->x1 = 2 * (p.x1 - a) - 4 * b*p.x1*(p.x2 - p.x1*p.x1);
  result->x2 = 2 * b*(p.x2 - p.x1*p.x1);
 }
 double getStep(const Point& point, const double& a, const double& b){
  Point x0(point.x1, point.x2);
  double p = 0.1;
  double step = 0.00001; // 初始化
  double bigger = 1.1; // 步长增大系数
  double smaller = 0.8; // 步长缩短系数
  Grad* g = new Grad();
  getGrad(point, a, b, g); // 得到梯度
  Point s_k(0 - step*g->x1, 0 - step*g->x2); // 负梯度方向乘步长
  Point x1(s_k.x1 + x0.x1, s_k.x2 + x0.x2);
  while (true){
   double bound = p*(g->x1*s_k.x1 + g->x2*s_k.x2);
   double f = (a - x1.x1)*(a - x1.x1) + b*(x1.x2 - x1.x1*x1.x1)*(x1.x2 - x1.x1*x1.x1) -
    (a - x0.x1)*(a - x0.x1) - b*(x0.x2 - x0.x1*x0.x1)*(x0.x2 - x0.x1*x0.x1);
   if (f <= bound){
    bound = (1 - p)*(g->x1*s_k.x1 + g->x2*s_k.x2);
    if (f >= bound) break;
    step *= bigger;
   }
   else{
    step *= smaller;
   }
   x0.x1 = x1.x1; x0.x2 = x1.x2;
   getGrad(point, a, b, g);
   s_k.x1 = 0 - step*g->x1; s_k.x2 = 0 - step*g->x2;
   x1.x1 = s_k.x1 + x0.x1; x1.x2 = s_k.x2 + x0.x2;
  }
  return step;
 }
 // 参数a和b是系数 二维函数
 vector<Point> rosenbrock(double& a, double& b){
  vector<Point> result;
  double bound = 0.000001;
  // 梯度
  Grad* g = new Grad();
  /*cout << "***********************" << endl;
  cout << g->x1 << " " << g->x2 << endl;
  cout << "**********************" << endl;*/
  Point x0 = { 9, 6 }; // 初始点
  result.push_back(x0);
  getGrad(x0, a, b, g); // 得到该点的梯度值
  //cout << g->x1 << " " << g->x2 << " " << endl;
  while (fabs(g->x1) > bound || fabs(g->x2) > 