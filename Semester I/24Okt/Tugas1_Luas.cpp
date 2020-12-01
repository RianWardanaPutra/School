#include <iostream>
#define PI 22/7.0
using namespace std;

double segi3(float alas, float tinggi);

int square(int sisi);

double lingk(int radius);
int sisi, alas, tinggi, radius;

int main(){
    int pilihMenu;
    double luas;
    cout << "\t~Menghitung Luas Segitiga, Persegi, dan Lingkaran~\n";
    while(true){
        cout << "Menu: \n"
        << "1. Lingkaran\n2. Persegi\n3. Segitiga\n4. Stop\n\n";
        cin >> pilihMenu;
        if(pilihMenu == 1){
            cout << "Menghitung luas lingkaran\n";
            cout << "Masukkan jari-jari: ";
            cin >> radius;
            luas = lingk(radius);
            cout << "Luas lingkaran = " << luas << endl << endl;
        }
        else if(pilihMenu == 2){
            cout << "Menghitung luas persegi\n";
            cout << "Masukkan sisi persegi: ";
            cin >> sisi;
            luas = square(sisi);
            cout << "Luas persegi = " << luas << endl << endl;
        }
        else if(pilihMenu == 3){
            cout << "Menghitung luas segitiga\n";
            cout << "Masukkan alas segitiga: ";
            cin >> alas;
            cout << "Masukkan tinggi segitiga: ";
            cin >> tinggi;
            luas = segi3(alas, tinggi);
            cout << "Luas segitiga = " << luas << endl << endl;
        }
        else if(pilihMenu == 4)
            break;
    }
    system("pause");
    return 0;
}

double segi3(float alas, float tinggi){
    double luas;
    luas = (alas*tinggi)/2;
    return luas;
}

int square(int sisi){
    int luas;
    luas = sisi*sisi;
    return luas;
}

double lingk(int radius){
    double luas;
    luas = radius*radius*PI;
    return luas;
}