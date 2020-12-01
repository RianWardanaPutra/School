//DatabaseBookStore.cpp
#include <iostream>
#include <vector>
//#include <fstream>
#include <algorithm>
#include <string>
#include <iomanip>

using namespace std;

int menu, pilihSort;
int x;

struct product{
    string judul;
    string creator;
    int noSerial;
    int jumlah;
    int edisi;
    int harga;
};

vector<product> book;

struct find_id : unary_function<product, bool> {
    int noSerial;
    find_id(int noSerial):noSerial(noSerial) { }
    bool operator()(product const& S) const {
        return S.noSerial == noSerial;
    }
};


void tambahList(vector<product> &book){
    product temp;
    int pilih;
    book.push_back(product());
    cout << "\n\t~Tambah List~\n";
    ulang:
    cout << "~ Masukkan No. Seri: ";
    cin >> temp.noSerial;
    cout << "~ Masukkan Judul buku (maks. 20 char): ";
    cin >> temp.judul;
    cout << "~ Masukkan Nama Pengarang (maks. 20 char): ";
    cin >> temp.creator;
    cout << "~ Masukkan Edisi buku: ";
    cin >> temp.edisi;
    cout << "~ Masukkan harga buku: ";
    cin >> temp.harga;
    cout << "~ Masukkan Jumlah buku: ";
    cin >> temp.jumlah;
    book.pop_back();
    book.push_back(temp);
    return;
}

bool hargaBuku(const product &a, const product &b) {
    return a.harga < b.harga;
}
bool edisiBuku(const product &a, const product &b){
    return a.edisi < b.edisi;
}
bool serialBuku(const product &a, const product &b){
    return a.noSerial < b.noSerial;
}
bool jumlahBuku(const product &a, const product &b){
    return a.jumlah < b.jumlah;
}


void sortAngka(vector<product>&book, int pilih){
    book.push_back(product());
    if(pilih==1){
        stable_sort(book.begin(), book.end(), serialBuku);
        
    }else if(pilih==2){
        stable_sort(book.begin(), book.end(), edisiBuku);
        
    }else if(pilih==3){
        stable_sort(book.begin(), book.end(), hargaBuku);
        
    }else if(pilih==4){
        stable_sort(book.begin(), book.end(), jumlahBuku);
        
    }
}

void sortChar(vector<product> &book, int pilih){
    if(pilih==1){
        sort(book.begin(), book.end(), [](const product &a, const product &b){
            return a.judul < b.judul;
        });
    }else if(pilih==2){
        sort(book.begin(), book.end(), [](const product &a, const product &b){
            return a.creator < b.creator;
        });
    }
}

void sortList(vector<product> &book){
    while(!pilihSort){
        cout << "\nIngin sort berdasarkan apa?";
        cout << "\n1. No. Serial\n2. Judul\n3. Pengarang\n4. Edisi\n5. Harga\n6. Jumlah\n";
        cin >> pilihSort;
        /*  Sort angka:
            1. Serial
            2. Edisi
            3. Harga
            4. Jumlah
            Sort char:
            1. Judul
            2. Pengarang
        */
        switch(pilihSort){
            case 1 : sortAngka(book, 1); break;
            case 2 : sortChar(book, 1); break;
            case 3 : sortChar(book, 2); break;
            case 4 : sortAngka(book, 2); break;
            case 5 : sortAngka(book, 3); break;
            case 6 : sortAngka(book, 4); break;
            default : cout << "Error, bukan masukkan!\n";
        }
    }
}

void lihatDaftar(vector<product> &book, int listSize){
    cout << left << setw(17) << "| No. Seri " << left << setw(24) << " | Judul " << left
    << setw(24) << " | Pengarang " << left << setw(8) << " | Ed. " << left << setw(12)
    << " | Harga " << left << setw(5) << " | Jml " << " | Jumlah Item = " << listSize << endl;
    for(int i=0; i<listSize; i++){
        cout << "| " << left << setw(15) << book[i].noSerial << " |" << left << setw(22) << book[i].judul << " |" << left << setw(22) << book[i].creator << " |"
        << left << setw(6) << book[i].edisi << " |" << left << setw(10) << book[i].harga << " |" << left << setw(5) << book[i].jumlah << " |\n";
    }
}

void pilihBuku(vector<product> &book);

void beli(vector<product> &book);

void pilihBuku(vector<product> &book){
    int i, listSize;
    int noSeri;
    bool found=0;
    listSize = static_cast<int>(book.size());
    lihatDaftar(book, listSize);
    cout << "Pilih buku berdasarkan nomor seri: ";
    cin >> noSeri;
    char pilih;
    for(i=0; i<listSize; i++){
        if(noSeri==book[i].noSerial){
            found=true;
            break;
        }
    }
    if(found){
        if(book[i].jumlah > 0){
            cout << "\n~!Buku ditemukan!~\n";
            cout << "Beli buku " << book[i].judul << " dari pengarang " << book[i].creator << " harga " << book[i].harga
            << "? (y/n)\n";
            cin >> pilih;
            if(pilih=='y'){
                book[i].jumlah--;
                cout << "Buku terbeli! Terimakasih!\n";
            }else {
                cout << "Pembelian dibatalkan!\n";
                return;
            }
        }else
            cout << "Buku habis, silakan pilih lagi\n";
    }else{
        cout << "Buku tidak ditemukan!\nKembali ke menu beli buku\n\n";
        beli(book);
    }
}
/*
void save(){
    ofstream inFile;
    inFile.open("Database.txt", ios::app);
    int listSize = book.size();
    for(int i=0; i<listSize; i++){
        inFile << book[i].noSerial << endl;
        inFile << book[i].judul << endl;
        inFile << book[i].creator << endl;
        inFile << book[i].edisi << endl;
        inFile << book[i].harga << endl;
        inFile << book[i].jumlah << endl;
        
    }
    inFile.close();
}

product master;

void load(){
    ifstream inFile;
    inFile.open("Database.txt", ios::app);
    int listSize = sizeof(inFile);
    for(int i=0; i<listSize; i++){
        inFile >> book[i].noSerial;
        getline(inFile, book[i].judul);
        getline(inFile, book[i].creator);
        inFile >> book[i].edisi;
        inFile >> book[i].harga;
        inFile >> book[i].jumlah;
        
    }
    inFile.close();
}*/


int main(){
    cout << "Store database 1.0\n";
    //load();
    do {
    cout << "\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" << endl;
    cout << "\t|~~~~~~~~~~~~~~~~~~Your Obvious BookStore~~~~~~~~~~~~~~~~~~~~~|\n";
    cout << left << setw(50) << "\t|\t\tMain Menu " << "|" << endl;
    cout << left << setw(50) << "\t|\t\t(1) Tambah " << "|" << endl;
    cout << left << setw(50) << "\t|\t\t(2) Sort " << "|" << endl;
    cout << left << setw(50) << "\t|\t\t(3) Lihat daftar " << "|" << endl;
    cout << left << setw(50) << "\t|\t\t(4) Beli " << "|" << endl;
    cout << left << setw(50) << "\t|\t\t(5) Keluar " << "|" << endl;
    cin >> menu;
    int listSize = book.size();
    switch(menu){
        case 1 : tambahList(book); break;
        case 2 : sortList(book); break;
        case 3 : lihatDaftar(book, listSize); break;
        case 4 : beli(book); break;
        case 5 : cout << "\n\t~Terima kasih!~~\n"; break;
        default : "\n\tInvalid input!";
    }
    }while(menu!=5);
    //save();
    return 0;
}

void beli(vector<product> &book){
    int pilih;
    int noSeri;
    cout << "\tMau beli buku apa?\n\n";
    cout << "1. Lihat daftar\n2. Kembali ke menu utama\n";
    cin >> pilih;
    switch(pilih){
        case 1 : pilihBuku(book); break;
        case 2 : return; break;
        default : cout << "Tidak ada dalam pilihan!\n"; break;
    }
    
    /*if(pilih==1){
        listSize = static_cast<int>(book.size());
        lihatDaftar(book, listSize);
        cout << "Pilih buku berdasarkan nomor seri: ";
        cin >> noSeri;
        pilihBuku(book, noSeri, listSize);
    }else if(pilih==2){
        return;
    }else{
        cout << "Tidak ada dalam pilihan\n";
        return;
    }*/
}