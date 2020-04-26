#include <iostream>
using namespace std;

// Struct of how the file is stored in the table
struct file
{
    char fname[10];
    int start, size, block[10];
}f[10];

int main(int argc, char const *argv[])
{
    int i,j,n;

    // Number files to stored
    cout << "Enter number of files: ";
    cin >> n;
    for (i = 0; i < n; i++)
    {
        // File details input
        cout << "Enter file name: ";
        cin >> f[i].fname;
        cout << "Enter starting block: ";
        cin >> f[i].start;
        f[i].block[0] = f[i].start;
        cout << "Enter number of blocks: ";
        cin >> f[i].size;
        cout << "Enter block numbers: ";
        for (j = 0; j < f[i].size; j++)
        {
            cin >> f[i].block[j];
        }
    }
    cout << "File\tstart\tsize\tblock\n";
    for (i = 0; i < n; i++)
    {
        cout << f[i].fname << "\t" << f[i].start << "\t" << f[i].size << "\t";
        for (j = 0; j < f[i].size; j++) 
        cout << f[i].block[j] << " --> ";
        cout << f[i].block[j];
        cout << endl;
    }
    return 0;
}
