#include <iostream>
using namespace std;

void increaseNumber(int i){
    cout << "* *" << endl;
    i++;
    if(i<10)
        increaseNumber(i);
}

int main(){
    
    int i = 0;
    increaseNumber(i);

    return 0;
}
