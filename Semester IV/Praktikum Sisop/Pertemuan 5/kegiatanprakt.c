/* Nama:   Fransiskus Rian Wardana Putra
 * NIM:    18/427592/PA/18552
 * gcc -v: 
 *     Thread model: posix
 *     gcc version 9.2.1 20200130 (Arch Linux 9.2.1+20200130-2)
 * Praktikum Sistem Operasi 23 Maret 2020 - Semaphore 
 * */

#include <stdio.h>

int main(int argc, char const *argv[])
{
    int buffer[10], bufsize=10, in=0, out=0, produce, consume,
        choice=0;
    while (choice != 3)
    {
        printf("\n1. Produce \t 2. Consume \t 3. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            if((in + 1) % bufsize == out)
                printf("\nBuffer is full!");
            else
            {
                printf("\nEnter the value: ");
                scanf("%d", &produce);
                buffer[in] = produce;
                in = (in+1) % bufsize;
            }
            break;
        
        case 2:
            if (in == out)
                printf("\nBuffer is empty");
            else
            {
                consume = buffer[out];
                printf("\nConsumed value is %d", consume);
                out = (out + 1) % bufsize;
            }
            break;
            
        default:
            break;
        }
    }
    
    return 0;
}
