#include <stdio.h>

int main(int argc, char const *argv[])
{
    int buffer[10], buffsize, in, out, produce, consume, choice=0;
    in=0;
    out=0;
    buffsize=10;
    while (choice!=3)
    {
        printf("\n1. Produce\n2. Consume\n3. Exit\n");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            if ((in+1) % buffsize == out) puts("\nBuffer is Full");
            else
            {
                puts("\nEnter the value: ");
                scanf("%d", &produce);
                buffer[in] = produce;
                in = (in+1) % buffsize;
            }
            break;
        case 2:
            if(in == out) puts("\nBuffer is Empty");
            else
            {
                consume = buffer[out];
                printf("\nThe consumed value is %d", consume);
                out = (out+1) % buffsize;
            }
            break;
        
        default:
            break;
        }
    }
    
    return 0;
}
