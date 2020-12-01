#include <iostream>
using namespace std;

void f(int *a){
    *a = 25;
}

int main(){
    int a=20;
    f(&a);
    cout << a;
    return 0;
}
