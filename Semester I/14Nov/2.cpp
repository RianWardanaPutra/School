#include <iostream>
using namespace std;

int Budi;
int Dodi;
int *Rani;
int *Sari;

int main(){
    Budi = 75;
    cout << "Budi = " << Budi << endl;
    cout << "&Budi = " << &Budi << endl;

    Dodi = Budi;
    cout << "Dodi = " << Dodi << endl;
    cout << "&Dodi = " << &Dodi << endl;

    Rani = &Budi;
    cout << "*Rani = " << *Rani << endl;
    cout << "Rani = " << Rani << endl;

    Sari = Rani;
    cout << "*Sari = " << *Sari << endl;
    cout << "Sari = " << Sari << endl;

    return 0;
}
