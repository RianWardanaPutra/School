#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

float R = 3.0;
double deltaX = 0.00001;

double f(double h)
{
    double V = (M_PI*h*h*(3*R-h)) - 90;
    return V;
}

double ff(double h)
{
    double x = 6*M_PI*R*h - 3*M_PI*h*h;
    return x;
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
