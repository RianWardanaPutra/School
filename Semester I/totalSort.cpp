//total Sort
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

void printArray(int A[], int size) 
{ 
	int i; 
	for (i=0; i < size; i++) 
		printf("%d ", A[i]); 
	printf("\n"); 
}

void merge(int arr[], int l, int m, int r);

//Merge sort!!
void mergeSort(int arr[], int l, int r) 
{ 
if (l < r) 
{ 
	int m = l+(r-l)/2; //Same as (l+r)/2 but avoids overflow for large l & h 
	mergeSort(arr, l, m); 
	mergeSort(arr, m+1, r); 
	merge(arr, l, m, r); 
} 
} 

/* Function to merge the two haves arr[l..m] and arr[m+1..r] of array arr[] */
void merge(int arr[], int l, int m, int r) 
{ 
	int i, j, k; 
	int n1 = m - l + 1; 
	int n2 = r - m; 

	/* create temp arrays */
	int L[n1], R[n2]; 

	/* Copy data to temp arrays L[] and R[] */
	for (i = 0; i < n1; i++) 
		L[i] = arr[l + i]; 
	for (j = 0; j < n2; j++) 
		R[j] = arr[m + 1+ j]; 

	/* Merge the temp arrays back into arr[l..r]*/
	i = 0; 
	j = 0; 
	k = l; 
	while (i < n1 && j < n2) 
	{ 
		if (L[i] <= R[j]) 
		{ 
			arr[k] = L[i]; 
			i++; 
		} 
		else
		{ 
			arr[k] = R[j]; 
			j++; 
		} 
		k++; 
	} 

	/* Copy the remaining elements of L[], if there are any */
	while (i < n1) 
	{ 
		arr[k] = L[i]; 
		i++; 
		k++; 
	} 

	/* Copy the remaining elements of R[], if there are any */
	while (j < n2) 
	{ 
		arr[k] = R[j]; 
		j++; 
		k++; 
	} 
} 


//insertion sort!!
void insertion(int data[], int dataSize){
    int i, j, temp;
    for(j=1; j<dataSize; j++){
		i=j-1;
		temp=data[j];
		while(data[i]>temp && i>=0){
			data[i+1] = data[i];
			i--;
		}
		data[i+1]=temp;
	}
}

//bubble sort
void bubble(int data[], int dataSize){
    int i, j, temp;
    for(int i=0; i<dataSize; i++){
		for(int j=0; j<dataSize-1; j++){
			if(data[j+1]<data[j]){
				temp=data[j];
				data[j]=data[j+1];
				data[j+1]=temp;
			}
		}
	}
}

//selection sort!!
int i, l, temp;
void selection(int data[], int dataSize){
    for(i=0; i<dataSize-1; i++){
		l=i;
		for(int j=i+1; j<dataSize; j++){
			if(data[j]<data[l]){
				l=j;
			}
		}
		temp=data[i];
		data[i] = data[l];
		data[l]=temp;
	}
}

int main(){
	int jumlah;
	cout << "~~FUNGSI SORT~~\n\n";
	cout << "Masukkan jumlah data: ";
	cin >> jumlah;
	cout << "Masukkan isi data acak: ";
	int data[jumlah];
	for(int i=0; i<jumlah; i++){
		cin >> data[i];
	}
	while(true){
		int pilih;
		cout << "Pilih menu: ";	
		cout << "Menu:\n\n1. Insertion sort\n2. Selection sort\n3. Buble sort\n4. Merge sort\n\n";
		cin >> pilih;
		if(pilih == 1){
			cout << "Data sebelum diubah:\n";
			printArray(data, jumlah);
			insertion(data, jumlah);
			cout << "\nData sesudah diubah:\n";
			printArray(data, jumlah);
			goto stop;
		}
		else if(pilih == 2){
			cout << "Data sebelum diubah:\n";
			printArray(data, jumlah);
			selection(data, jumlah);
			cout << "\nData sesudah diubah:\n";
			printArray(data, jumlah);
			goto stop;
		}
		else if(pilih == 3){
			cout << "Data sebelum diubah:\n";
			printArray(data, jumlah);
			bubble(data, jumlah);
			cout << "\nData sesudah diubah:\n";
			printArray(data, jumlah);
			goto stop;
		}
		else if(pilih == 4){
			int dataSize = sizeof(data)/sizeof(data[0]);
			cout << "Data sebelum diubah:\n";
			printArray(data, jumlah);
			mergeSort(data, 0, dataSize - 1);
			cout << "\nData sesudah diubah:\n";
			printArray(data, jumlah);
			goto stop;
		}
	}
	stop:
		system("pause");
	return 0;
}
