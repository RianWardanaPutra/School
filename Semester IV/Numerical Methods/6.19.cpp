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
    for(int i = 0; i < 100; i++)
    {
        if(count((low + high) / 2) < 30)
        {
            low = (low + high) / 2;
            cout << "low: " << low << endl;
        }
        else
        {
            high = (low + high) / 2;
            printf("high: %lf\n", high);
        }
    }
    cout << "low: " << low << ", count: " << count(low) << endl;
    cout << "high: " << high << ", count: " << count(high) << endl;
    return 0;
}