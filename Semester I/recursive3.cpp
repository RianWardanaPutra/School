#include <iostream>
using namespace std;

void increaseNumber(int i){
    for(int j = 0; j < i; j++){
        cout << "* ";
    }
    i++;
    cout << endl;
    if(i<10)
        increaseNumber(i);
}

int main(){
    
    int i = 0;
    increaseNumber(i);

    return 0;
}