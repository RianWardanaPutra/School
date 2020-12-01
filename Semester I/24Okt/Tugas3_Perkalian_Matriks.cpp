#include <iostream>
using namespace std;

int i, j;

void masuk(int matriks1[][10], int matriks2[][10], int baris1, int kolom1, int baris2, int kolom2);

void kali(int matriks1[][10], int matriks2[][10], int hasil[][10], int baris1, int kolom1, int baris2, int kolom2);

void display(int hasil[][10], int baris1, int kolom2);

void display1(int matriks1[][10], int baris1, int kolom1);

void display2(int matriks2[][10], int baris2, int kolom2);

int main(){
    int matriks1[10][10], matriks2[10][10], hasil[10][10], baris1, kolom1, baris2, kolom2, i, j, k;
    cout << "Matriks 1:\n Masukkan baris: ";
    cin >> baris1;
    cout << " Masukkan kolom: ";
    cin >> kolom1;
    cout << "Matriks 2:\n Masukkan baris: ";
    cin >> baris2;
    cout << " Masukkan kolom: ";
    cin >> kolom2;

    while(kolom1 != baris2){
        cout << "Error! kolom matriks 1 tidak sama dengan baris matriks 2!"
        << "\nMasukkan ulang!";
        cout << "Matriks 1:\n Masukkan baris: ";
        cin >> baris1;
        cout << " Masukkan kolom: ";
        cin >> kolom1;
        cout << "Matriks 2:\n Masukkan baris: ";
        cin >> baris2;
        cout << " Masukkan kolom: ";
        cin >> kolom2;   
    }
    masuk(matriks1, matriks2, baris1, kolom1, baris2, kolom2);

    display1(matriks1, baris1, kolom1);

    display2(matriks2, baris2, kolom2);
    
    kali(matriks1, matriks2, hasil, baris1, kolom1, baris2, kolom2);

    display(hasil, baris1, kolom2);

}

void masuk(int matriks1[][10], int matriks2[][10], int baris1, int kolom1, int baris2, int kolom2){
    int i, j;
    cout << "Masukkan elemen matriks 1:\n";
    for(i=0; i<baris1; i++){
        for(j=0; j<kolom1; j++){
            cout << "Masukkan elemen matriks1 a" << i+1 << j+1 << ": ";
            cin >> matriks1[i][j];
        }
    }
    cout << "Masukkan elemen matriks 2:\n";
    for(i=0; i<baris2; i++){
        for(j=0; j<kolom2; j++){
            cout << "Masukkan elemen matriks2 b" << i+1 << j+1 << ": ";
            cin >> matriks2[i][j];
        }
    }
}

void kali(int matriks1[][10], int matriks2[][10], int hasil[][10], int baris1, int kolom1, int baris2, int kolom2){
    int i, j, k;
    for(i=0; i<baris1; i++){
        for(j=0; j<kolom2; j++){
            hasil[i][j] = 0;
        }
    }
    for(i=0; i<baris1; i++){
        for(j=0; j<kolom2; j++){
            for(k=0; k<kolom1; k++){
                hasil[i][j] += matriks1[i][k] * matriks2[k][j];
            }
        }
    }
}

void display1(int matriks1[][10], int baris1, int kolom1){
    int i, j;
    cout << "Matriks 1:\n";
    for(i=0; i<baris1; i++){
        for(j=0; j<kolom1; j++){
            cout << matriks1[i][j] << "  ";
        }
        cout << endl << endl;
    }
}

void display2(int matriks2[][10], int baris2, int kolom2){
    int i, j;
    cout << "Matriks 2:\n";
    for(i=0; i<baris2; i++){
        for(j=0; j<kolom2; j++){
            cout << matriks2[i][j] << "  ";
        }
        cout << endl << endl;
    }
}

void display(int hasil[][10], int baris1, int kolom2){
    int i, j;
    cout << "Hasil perkalian matriks:\n";
    for(i=0; i<baris1; i++){
        for(j=0; j<kolom2; j++){
            cout << hasil[i][j] << "  ";
        }
        cout << endl << endl;
    }
}
