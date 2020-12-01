#include <iostream>
#include <vector>

using namespace std;

struct sesuatu{
    int b;
    string c;
};



int main(){
    int n, f;
    cin >> n;
    vector<sesuatu> nums;

    for(int i=0; i<n; i++){
        sesuatu temp;
        cin >> temp.c;
        temp.b = i;
        nums.push_back(temp);
    }
    f = nums.size();
    cout << endl << f << endl;
}