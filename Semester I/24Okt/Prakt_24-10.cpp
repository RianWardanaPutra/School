#include <iostream>
using namespace std;
const int pi = 3.14159265;

double getArea(double radius);

int main(){
    double radius = 1.1, area1, area2;
    area1 = getArea(radius);
    cout << "area 1 is " << area1 << endl;
    area2 = getArea(2.2);
    cout << "area 2 is " << area2 << endl;
    cout << "area 3 is " << getArea(3.3) << endl;
}

double getArea(double radius){
    return radius*radius*pi;
}