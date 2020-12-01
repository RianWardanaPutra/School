#include <iostream>
#include <cmath>
#define pi 22/7.0
using namespace std;

double selimut(float r, float s){
	double luas;
	luas = pi * r * s;
	return luas;
}

double alas(float r){
	double luas;
	luas = r*r*pi;
	return luas;
}

double pelukis(float tinggi, float r){
	float pelukis;
	pelukis = sqrt(pow(tinggi, 2)+pow(r, 2));
	return pelukis;
}

double volume(double luas, float tinggi){
	double volume;
	volume = luas * tinggi /3;
	return volume;
}

float r, s, t;

int main(){
	double luas, juring, lingk, volum;
	cout << "Masukkan jari-jari: ";
	cin >> r;
	cout << "Masukkan tinggi kerucut: ";
	cin >> t;
	s = pelukis(t, r);
	juring = selimut(r, s);
	lingk = alas(r);
	luas = lingk + juring;
	volum = volume(lingk, t);
	cout << "Luas permukaan kerucut = " << luas << endl;
	cout << "Volume kerucut = " << volum << endl;
	return 0;
}
