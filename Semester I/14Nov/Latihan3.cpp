#include <iostream>
using namespace std;

void swap(int &a, int &b){
    int c;
    c=a;
    a=b;
    b=c;
}

int main(){
    int a,b;
    a = 4;
    b = 5;
    swap(a, b);
    cout << "a = " << a << " b = " << b << endl;
}