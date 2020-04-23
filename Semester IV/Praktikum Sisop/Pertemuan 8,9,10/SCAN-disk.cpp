#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    float avg;
    int sectors[100], head, n_sectors, totalSeek, count=0;

    // I put this code here because I found strange
    // behavior of my code. It marked sectors 68, 72, 83 out of the blue.
    for (int i = 0; i < 100; i++)
    {
        sectors[i] = 0;
    }

    cout << " *** SCAN(Elevate) Disk Management Algorithm ***\n" << endl;
    
    // In os sim the total of sectors is 192 sectors,
    // within 16 cylinders in which has 12 sectors each.
    // Here, I use only 100 sectors just to simulate the algorithm.
    cout << "Total of available sectors = 100" << endl;
    
    // The total of sectors that will be served
    cout << "Enter number of sectors: ";
    cin >> n_sectors;

    // The sectors that will be served
    cout << "Enter the sectors:" << endl;
    for (int i = 0; i < n_sectors; i++)
    {
        int sector;
        cout << "Input sector: ";
        cin >> sector;

        // Mark the sector location
        sectors[sector] = 1;
    }

    // Prints the sectors
    cout << "[ ";
    for (int i = 0; i < 100; i++)
    {
        if(sectors[i] == 1)
        cout << i << " ";
    }
    cout << "]" << endl;

    // The position of the head which the disk will be started from
    cout << "Enter head position: ";
    cin >> head;

    // The algorithm is running from head position,
    // scanning through the disk until the end of sectors,
    // then moving backward scanning until the start of the disk.
    for (int j = 0; j < (100 - head); j++)
    {
        // If the marked sector found, calculate the seek time
        // and add it to total seek time, and mark the sector
        // to indicate the sector has been processed.
        if (sectors[head + j] == 1)
        {
            sectors[head + j] = 2;
            if (count == 1)
            {
                cout << "Seek " << count << "\ttime from last sector. Current sector number: " << (head+j) << endl;
            }
            else 
            {
                cout << "Seek " << count << "\ttimes from last sector. Current sector number: " << (head+j) << endl;
            }
            totalSeek += count;

            // Reset the count so it can calculate the seek time
            // between this sector and the next sector found.
            count = 0;
        }
        count++;
    }

    // Doing the same as above, but in reverse order
    // from the end of sector to the start of the disk
    for (int k = 99 - 1; k >= 0; k--)
    {
        if (sectors[k] == 1)
        {
            sectors[k] = 2;
            if (count == 1)
            {
                cout << "Seek " << count << "\ttime from last sector. Current sector number: " << k << endl;
            }
            else 
            {
                cout << "Seek " << count << "\ttimes from last sector. Current sector number: " << k << endl;
            }
            totalSeek += count;
            count = 0;
        }
        count++;
        
    }

    cout << "Total seek time until last sector served is: " << totalSeek << endl;
    avg = totalSeek/(float)n_sectors;
    cout << "Average seek time is: " << avg << endl;

    return 0;
}
