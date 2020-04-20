#include <stdio.h>
#include <conio.h>
#include <math.h>

int tph, philname[20], status[20], howhung, hu[20], cho;

int one()
{
    int pos=0, x, i;
    printf("\nAllow one philosopher to eat at any time\n");

    // just grant hungry phils to eat
    // one phils a time
    for (int i = 0; i < howhung; i++, pos++)
    {
        printf("\nP %d is granted to eat", philname[hu[pos]]);
        for(x=pos; x<howhung; x++)
            printf("\nP %d is waiting", philname[hu[x]]);
    }
}

int two()
{
    int i, j, s=0, t, r, x;
    printf("\nAllow two philosophers to eat at same time\n");
    for(i=0; i<howhung; i++)
    {
        for (j = 0; j < howhung; j++)
        {

            // for every combination of i and j
            // it is not possible for hungry phils no i and j
            // to eat together if they're positioned side by side.
            // phils i - phils j MUST be more than 1
            // this section is originally abs(hu[i] - hu[j] >= 1)
            // the new condition is to avoid eating phils sits next to each other
            // also removed abs(hu[i] - hu[j] != 4)
            // changing it to the new one below
            // to avoid first and last phils allowed to eat
            if (abs(hu[i] - hu[j]) > 1 && abs(hu[i] - hu[j]) != (hu[howhung-1]))
            {
                printf("\n\ncombination %d \n", (s+1));
                t=hu[i];
                r=hu[j];
                s++;
                printf("\nP %d and P %d are granted to eat", philname[hu[i]], philname[hu[j]]);
                for(x=0; x<howhung; x++)
                {
                    if((hu[x] != t) && (hu[x] != r))
                    {
                        printf("\nP %d is waiting", philname[hu[x]]);
                    }
                }
            }   
        }
    }
}

int main(int argc, char const *argv[])
{
    int i;
    printf("\n\nDINING PHILOSOPHER PROBLEM\n");
    printf("\nEnter the total no. of philosophers: ");

    // Store number of philosophers
    // and set all philosophers status to 1
    scanf("%d", &tph);
    for(i=0; i<tph; i++)
    {
        philname[i] = (i+1);
        status[i] = 1;
    }

    // Store number of hungry philosophers (or philosophers that will be allowed to eat)
    printf("How many are hungry: ");
    scanf("%d", &howhung);

    // if hungry phils == total phils
    // reject the number, as deadlock would occurs
    if(howhung == tph)
    {
        printf("\nAll are hungry...\nDeadlock stage will occur\n");
        printf("\nExiting...\n");
    }
    else
    {
        // Store hungry phils' position
        for(i=0; i<howhung; i++)
        {
            printf("Enter philosopher %d position (starts from 1): ", (i+1));
            scanf("%d", &hu[i]);

            // reduce the entered number for convention
            hu[i]--;

            // set the hungry phils' status to 2
            // compared to the others (1)
            status[hu[i]]=2;
        }

        do
        {
            printf("\n1. One can eat at a time\n2. Two can eat at a time\nEnter your choice: ");
            scanf("%d", &cho);
            switch (cho)
            {
            case 1:
                one();
                break;
            case 2:
                two();
                break;
            default:
                printf("\nInvalid option...\n");
                break;
            }
        } while (1);
        
    }
    return 0;
}
