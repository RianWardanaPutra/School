#include <iostream>
using namespace std;
int i, a, b;


int main(){
    int titik;
    string gambar;
    cin >> titik;
    for(i=0; i<=titik; i++){
        for(a=titik-i; a>1; a--){
            cout << " ";
        }
        cout << "X";
        for(b=1; b<=titik; b++)
            cout << " ";
    }
}