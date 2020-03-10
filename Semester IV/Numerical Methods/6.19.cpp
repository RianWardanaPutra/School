#include <iostream>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

double count(double h)
{
    double V = (M_PI*pow(h, 2))*(3-(h/3));
    return V;
}

int main(int argc, char const *argv[])
{
    double low = 0;
    double high = 10;
    for(int i = 0; i < 3; i++)
    {
        if(count((low + high) / 2) < 30)
        {
            cout << "low: " << low << ", count(low): " << count(low) << endl;
            low = (low + high) / 2;
        }
        else
        {
            printf("high: %lf, count(high): %lf\n", high, count(high));
            high = (low + high) / 2;
        }
    }
    cout << "final low: " << low << ", count: " << count(low) << endl;
    cout << "final high: " << high << ", count: " << count(high) << endl;
    printf("Result H after 3 iterations, H: %lf, count(H): %lf\n", (high+low/2.0), count((high+low)/2.0));
    return 0;
}
