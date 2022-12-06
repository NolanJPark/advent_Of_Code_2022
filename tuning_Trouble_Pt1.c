#include <stdio.h>
#define SIZE 4 //make SIZE 14 for part 2 since it's just a difference in how many characters have to be different not the process

int main()
{
    int first = 0;
    int a[SIZE] = {0};
    FILE *fp = fopen("tuning_Trouble_File.txt", "r");
    while (!feof(fp))
    {
        int c = (int)fgetc(fp);
        first++;
        if (first <= SIZE)
            a[first - 1] = c;
        else
        {
            for (int i = 0; i < SIZE; i++)
            {
                if (i == SIZE - 1)
                    a[SIZE-1] = c;
                else
                    a[i] = a[i+1];

            }
            if (check(a) == 1)
                break;
        }
    }
    printf("The first marker is after character %d", first);
}

int check(int a[])
{
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = i+1; j < SIZE; j++)
        {
            if (a[i] == a[j])
                return 0;
        }
    }
    return 1;
}
