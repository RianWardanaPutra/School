#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

double B = 20.0;
double s = 0.0002;
double Q = 5;
double n = 0.03;
double deltaX = 0.000001;

double f(double x)
{
    double a = sqrt(s)*(pow((B*x), (5.0/3)));
    double b = (Q * n * (pow(B+2*x, (2.0/3))));
    return a-b;
}

double ff(double x)
{
    double a = (pow(20, 5.0/3)*pow(x, 2.0/3))/(15*pow(2,3.0/2)) - \
                (1.0/(5*pow(2*x+20,1/3.0)));
    return a;
}

double newton(double x)
{
    double result = (x - (f(x)/ff(x)));
    return result;
}

double secant(double x)
{
    double result = x - (f(x)*deltaX)/(f(x+deltaX)-f(x));
    return result;
}

int main(int argc, char const *argv[])
{
    printf("Newton Method:\n");
    double X = 1;
    for(int i = 0; i < 10; i++)
    {
        printf("X: %lf, f(X): %lf\n", X, f(X));
        X = newton(X);
    }

    printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("Secant Method:\n");
    double Y = 1;
    for(int i = 0; i < 10; i++)
    {
        printf("X: %lf, f(X): %lf\n", Y, f(Y));
        Y = secant(Y);
    }
    return 0;
}
