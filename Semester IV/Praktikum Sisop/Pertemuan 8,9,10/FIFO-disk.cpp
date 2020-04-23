#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int queue[100], n, head, seek=0, diff;
    float avg;

    cout << "*** FCFS Disk Scheduling Algorithm ***\n";

    // The number of queue, it is the number of total sectors
    // will be served by disk.
    cout << "Enter the size of Queue\t:";
    cin >> n;

    // Input the sector position within the disk
    cout << "Enter the Queue :" << endl;
    for (int i = 1; i <= n; i++)
    {
        cout << "queue[" << i << "]: ";
        cin >> queue[i];
    }

    // The position of the head which the disk will be started from
    cout << "Enter the initial head position\t:";
    cin >> head;
    queue[0] = head;
    cout << endl;

    // The algorithm is quite simple.
    // Because the algorithm is first come first served,
    // the seek time is calculated by difference of
    // each sector in queue
    for (int j = 0; j < n; j++)
    {
        diff = abs(queue[j+1]-queue[j]);

        // Here the total seek time added
        // by the seek time of each sequence
        seek += diff;
        cout << "Move from " << queue[j] << " to " << queue[j+1] << " with Seek " << diff << endl;
    }
    
    cout << "\nTotal Seek Time is " << seek << "\t";
    avg = seek/(float)n;
    cout << "\nAverage Seek Time is " << avg << endl;
    return 0;
}
