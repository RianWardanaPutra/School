#include <iostream>
using namespace std;



int main(){
    int x = 10;
    int *p;
    p = &x;
    cout << &p << endl;
    cout << *p << endl;
    cout << *(&x) << endl;
}