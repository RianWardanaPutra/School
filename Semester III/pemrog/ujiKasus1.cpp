#include <iostream>
using namespace std;

int x,d=0,e=0,f=0,total_harga=0;
string disc;
struct beli{
	string nama_es;
	int harga_es;
}es_krim[500];

void menu_es(){
	int pilih;
	int coklat = 15000;
	int vanila = 20000;
	int ubi = 25000;
	menu:
	cout<<"MENU : "<<endl;
	cout<<"1. Es Krim Coklat (Rp. 15.000)"<<endl;
	cout<<"2. Es Krim Vanila (Rp. 20.000)"<<endl;
	cout<<"3. Es Krim Ubi (Rp. 25.000)"<<endl;
	cout<<"4. Selesai Membeli"<<endl;
	cout<<"Pilih Es Krim : ";cin>>pilih;
	switch(pilih){
		case 1:{
			if(d>=1){
				cout<<"Mohon maaf anda tidak dapat membeli es krim jenisnya sama pada sekali transaksi"<<endl;
				goto menu;
			}
			es_krim[x].nama_es="Coklat";
			es_krim[x].harga_es=15000;
			total_harga=total_harga+es_krim[x].harga_es;
			d++;
			x++;
			goto menu;
		}
		case 2:{
			if(e>=1){
				cout<<"Mohon maaf anda tidak dapat membeli es krim jenisnya sama pada sekali transaksi"<<endl;
				goto menu;
			}
			es_krim[x].nama_es="Vanila";
			es_krim[x].harga_es=20000;
			total_harga=total_harga+es_krim[x].harga_es;
			e++;
			x++;
			goto menu;
		}
		case 3:{
			if(f>=1){
				cout<<"Mohon maaf anda tidak dapat membeli es krim jenisnya sama pada sekali transaksi"<<endl;
				goto menu;
			}
			es_krim[x].nama_es="Ubi";
			es_krim[x].harga_es=25000;
			total_harga=total_harga+es_krim[x].harga_es;
			f++;
			x++;
			goto menu;
		}
		case 4:{
			break;
		}
		default:{
			goto menu;
		}
	}
}

int main(){
	string nama_pembeli;
	int uang_bayar,potongan,total_bayar;
	cout<<"=============================="<<endl;
	cout<<"\t~~CM ICE CREAM~~"<<endl;
	cout<<"=============================="<<endl;
	cout<<"Nama Pembeli : ";getline(cin, nama_pembeli);
	menu_es();
	system("cls");
	output:
	cout<<"\t CM ICE CREAM "<<endl;
	cout<<"=========================="<<endl;
	cout<<"Nama Pembeli \t\t"<<nama_pembeli<<endl;
	for (int y=0;y<x;y++){
		cout<<es_krim[y].nama_es<<"\t\t 1 x \t"<<es_krim[y].harga_es<<endl;
	}
	cout<<"Jumlah Es Krim \t\t"<<d+e+f<<endl;
	cout<<"Total Harga \t\t"<<total_harga<<endl;
	if(total_harga>50000){
		total_bayar=total_harga*90/100;
		disc="10%";
	}else if(total_harga>40000 && total_harga<=50000){
		total_bayar=total_harga*95/100;
		disc="5%";
	}else{
		total_bayar=total_harga;
		disc="0%";
	}
	cout<<"Potongan \t\t"<<disc<<endl;
	cout<<"Total Keseluruhan \t"<<total_bayar<<endl;
	cout<<"Uang Bayar \t\t";cin>>uang_bayar;
	if(uang_bayar<total_bayar){
		cout<<"Uang anda tidak mencukupi untuk melakukan transaksi ini"<<endl;
		getchar();
		system("cls");
		goto output;
	}
	cout<<"Uang Kembalian \t\t"<<uang_bayar-total_bayar<<endl;
	cout<<"\t Terimakasih!!!!"<<endl;
	return 0;
}
