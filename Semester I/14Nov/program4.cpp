#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    int var_x = 273;
    int *ptr1;
    int **ptr2;
    ptr1 = &var_x;
    ptr2 = &ptr1;
    cout << "Nilai var_x = *ptr1 = " << *ptr1 << endl;
    cout << "Nilai var_x = **ptr2 = " << **ptr2 << endl;
    cout << "ptr1 = &var_x = " << ptr1 << endl;
    cout << "ptr2 = &ptr1 = " << ptr2 << endl;
    cout << "       &ptr2 = " << &ptr2 << endl;

    return 0;
}