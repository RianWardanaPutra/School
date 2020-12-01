#include <iostream>
using namespace std;
double pi = 22/7.0;

double luasSegi3(int alas, int tinggi){
    double luas;
    luas = (alas * tinggi)/2.0;
    return luas;
};

double luasO(int radius){
    double luas;
    luas = radius * radius * pi;
    return luas;
};

int luasSQ(int sisi){
    int luas;
    luas = sisi * sisi;
    return luas;
};
int alas, tinggi, sisi, radius;

int main(){
    while (true){
        int pilih;
        cout << "Pilih Menu : \n\n";
        cout << "1. Luas Segitiga\n2. Luas Lingkaran\n3. Luas Persegi\n4. Stop\n\n";
        cin >> pilih;
        double luasS3, luasLingk;
        int luasK;
        if(pilih == 1){
            cout << "Masukkan alas: ";
            cin >> alas;
            cout << "Masukkan tinggi: ";
            cin >> tinggi;
            luasS3 = luasSegi3(alas,tinggi);
            cout << "Luas Segitiga = " << luasS3 << endl;
        }
        else if(pilih == 2){
            cout << "Masukkan jari-jari: ";
            cin >> radius;
            luasLingk = luasO(radius);
            cout << "Luas lingkaran = " << luasLingk << endl;
        }
        else if(pilih == 3){
            cout << "Masukkan panjang sisi: ";
            cin >> sisi;
            luasK = luasSQ(sisi);
            cout << "Luas persegi = " << luasK << endl;
        }
        else if(pilih == 4)
            break;
    }    
}