#include <iostream>
using namespace std;

int main(){
	int data[]={0, 5, 31, 4, 6, 7, 8, 9, 42, 3, 22, 11, 1, 2, 5};
	int i, dataSize = sizeof(data)/sizeof(data[0]), min, temp;
	for(int i=0; i<dataSize-1; i++){
		min=i;
		for(int j=i+1; j<dataSize; j++){
			if(data[j]<data[min]){
				min=j;
			}
		}
		temp=data[i];
		data[i] = data[min];
		data[min]=temp;
	}
	for(int i=0; i<dataSize; i++){
		cout << data[i] << " ";
	}
	return 0;
}
