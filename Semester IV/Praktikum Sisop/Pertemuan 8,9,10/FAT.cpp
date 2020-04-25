#include <iostream>


struct file
{
    char fname[10];
    int start, size, block[10];
}f[10];

int main(int argc, char const *argv[])
{
    int i,j,n;
    std::cout << "Enter number of files: ";
    std::cin >> n;
    for (i = 0; i < n; i++)
    {
        std::cout << "Enter file name: ";
        std::cin >> f[i].fname;
        std::cout << "Enter starting block: ";
        std::cin >> f[i].start;
        f[i].block[0] = f[i].start;
        std::cout << "Enter number of blocks: ";
        std::cin >> f[i].size;
        std::cout << "Enter block numbers: ";
        for (j = 0; j < f[i].size; j++)
        {
            std::cin >> f[i].block[j];
        }
    }
    std::cout << "File\tstart\tsize\tblock\n";
    for (i = 0; i < n; i++)
    {
        std::cout << f[i].fname << "\t" << f[i].start << "\t" << f[i].size << "\t";
        for (j = 0; f[i].size; j++) std::cout << f[i].block[j] << " --> ";
        std::cout << f[i].block[j];
        std::cout << std::endl;
    }
    return 0;
}
