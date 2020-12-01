#include <iostream>
#include <cstdlib>
using namespace std;

void merge(int arr[], int l, int m, int r){
	int i, j, k;
	int n1=m-l+1;
	int n2=r-m;

	int L[n1], R[n2];

	for(i=0; i<n1; i++)
		L[i] = arr[l+1];
	for(j=0; j<n2; j++)
		R[j] = arr[m+1+j];

	i=0;
	j=0;
	k=l;
	
	while(i<n1 && j<n2){
		if(L[i] <= R[j]){
			arr[k] = L[i];
			i++;
		}
		else{
			arr[k] = R[j];
			j++;
		}
		k++;
	}
	while(i<n1){
		arr[k] = L[i];
		i++;
		k++;
	}
}

void mergeSort(int arr[], int l, int r){
	if(l<r){
		int m=l+(r-l)/2;
		mergeSort(arr, l, m);
		merge(arr, l, m, r);
	}
}

void printArray(int a[], int size){
	int i;
	for(i=0; i<size; i++)
		cout << a[i] << " ";
	cout << endl;
}

int main(){
	int data[]={0, 5, 3, 6, 7, 1};
	int i, dataSize = sizeof(data)/sizeof(data[0]), temp;
	cout << "Data sebelum disort: \n";
	printArray(data, dataSize);
	mergeSort(data, 0, dataSize-1);
	cout << "Data setelah sort: \n";
	printArray(data, dataSize);
	return 0;
}
