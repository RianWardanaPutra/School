//test UAS
#include <iostream>
using namespace std;

void hitung(int x, int y, int z){
    if(y==0){
        cout << z << endl;
    }else{
        if(y%2==1){
            z=z+x;
        }
        hitung(2*x,y/2,z);
    }
}

int main(int argc, const char* argv[]){
    while(true){
        int x, y, z;
        cout << "Input x: ";cin >> x;
        cout << "Input y: ";cin >> y;
        cout << "Input z: ";cin >> z;
        hitung(x,y,z);
    }
    return 0;
}