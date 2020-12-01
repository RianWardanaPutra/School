#include <iostream>
using namespace std;

int main(){
	int data[]={0, 5, 31, 4, 6, 7, 8, 9, 42, 3, 22, 11, 1, 2, 5};
	int i, dataSize = sizeof(data)/sizeof(data[0]), temp;
	for(int i=0; i<dataSize; i++){
		for(int j=0; j<dataSize-1; j++){
			if(data[j+1]<data[j]){
				temp=data[j];
				data[j]=data[j+1];
				data[j+1]=temp;
			}
		}
	}
	for(int j=0; j<dataSize; j++){
		cout << data[j] << " ";
	}
	return 0;
}
