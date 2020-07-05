#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int queue[100], n, head, seek=0, diff;
    float avg;

    cout << "*** FCFS Disk Scheduling Algorithm ***\n";

    cout << "Enter the size of Queue\t:";
    cin >> n;

    cout << "Enter the Queue :" << endl;
    for (int i = 1; i <= n; i++)
    {
        cout << "queue[" << i << "]: ";
        cin >> queue[i];
    }

    cout << "Enter the initial head position\t:";
    cin >> head;
    queue[0] = head;
    cout << endl;

    for (int j = 0; j < n; j++)
    {
        diff = abs(queue[j+1]-queue[j]);

        seek += diff;
        cout << "Move from " << queue[j] << " to " << queue[j+1] << " with Seek " << diff << endl;
    }
    
    cout << "\nTotal Seek Time is " << seek << "\t";
    avg = seek/(float)n;
    cout << "\nAverage Seek Time is " << avg << endl;
    return 0;
}
