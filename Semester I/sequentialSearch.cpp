#include <iostream>
using namespace std;

int main(){
    bool found=false;
    const char* nama[]={"Adi","budi","Charlie","Dodi","Edi"};
    const char* nomorInduk[]={"10101","10103","10105","10102","10104"};
    const char* query="10104";
    float nilai[]={64.75,75.11,84.63,77.07,66.70};
    for( int i=0; i<5; i++){
        if (nomorInduk[i]==query){
            cout << nama[i]<<","<<nomorInduk[i]<<","<<nilai[i]<<endl;
            found=true;
        }
    }
    if(!found){
        cout << "Tidak ditemukan!";
    }
    return 0;
}
