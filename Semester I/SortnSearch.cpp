#include <utility>
#include <iostream>
using namespace std;

struct data{
    const char* nama;
    int nilai;
    long nisn;
};

data mhs[10];


long partition (data arr[], int low, int high)
{
    int pivot = arr[high];    // pivot
    int i = (low - 1);  // Index of smaller element
 
    for (int j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return (i + 1);
}
 
/* The main function that implements QuickSort
 arr[] --> Array to be sorted,
  low  --> Starting index,
  high  --> Ending index */
void quickSort(data arr[], int low, int high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        int pi = partition(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}
/* Function to print an array */
void printArray(long arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        cout << arr[i] << "\n";
    printf("\n");
}
void printArrayInt(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        cout << arr[i] << "\n";
    printf("\n");
}
void printArrayChr(const char* arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        cout << arr[i] << "\n";
    printf("\n");
}


int main(){
    long NISN[]={9960312699,9963959682,9950310962,9970272750,9970293945,9952382180,9965653989};
    const char* nama[]={"Handi Ramadhan","Rio Alfandra","Ronaldo Valentino Uneputty","Achmad Yaumil Fadjri R.", "Alivia Rahma Pramesti","Ari Lutfianto","Arief Budiman"};
    int nilai[]={90,55,80,60,70,65,60};
    int n = sizeof(NISN)/sizeof(NISN[0]);
    for(int i=0; i<n; i++){
        mhs[i].nama = nama[i];
        mhs[i].nilai = nilai[i];
        mhs[i].nisn = NISN[i];
    }
    for(int i = 0; i<n;i++){
        cout << endl;
        cout << mhs[i].nama << endl;
        cout << mhs[i].nisn << endl;
        cout << mhs[i].nilai << endl;
        cout << endl;
    }

    quickSort(mhs.nisn, 0, n-1);
    printArrayChr(nama, n);
    return 0;
}