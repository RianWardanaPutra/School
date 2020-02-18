#include <iostream>
#include <math.h>

using namespace std;

double count(double h)
{
    double B = 20.0;
    double s = 0.0002;
    double Q = 5;
    double n = 0.03;
    double a = sqrt(s)*(pow((B*h), (5.0/3)));
    double b = (Q * n * (pow(B+2*h, (2.0/3))));
    // cout << "a: " << a << " b: " << b << endl;
    return a-b;
}

int main(int argc, char const *argv[])
{
    double low = 0;
    double high = 1;
    for (int i = 0; i < 10; i++)
    {
        double x = count((low + high) / 2);
        if (x > 0)
        {
            // cout << "High: " << high << endl;
            high = (high + low) / 2;
        }
        else
        {
            // cout << "Low: " << low << endl;
            low = (high + low) / 2;
        }
        
    }
    // cout << "0.7: " << count(0.7) << endl;
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("low: %lf => result low: %f\n", low, count(low));
    printf("high: %lf => result high: %f\n", high, count(high));
    return 0;
}
