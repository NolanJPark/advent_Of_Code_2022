/*

*/

#include <stdio.h>

int main()
{
    int tot = 0;
    FILE *fp = fopen("camp_Cleanup_File.txt", "r");
    while (!feof(fp))
    {
        int p11, p12, p21, p22;
        fscanf(fp, "%d-%d,%d-%d\n", &p11, &p12, &p21, &p22);
        int a1[p12 - p11 + 1], a2[p22 - p21 + 1];
        fill (a1, a2, p11, p12, p21, p22);
        if (test(a1, a2, p12 - p11 + 1, p22 - p21 + 1))
            tot++;
    }
    printf("In %d many assignment pairs the ranges overlap", tot);
    fclose(fp);
}

void fill(int a1[], int a2[], int p11, int p12, int p21, int p22)
{
    int j = 0;
    for (int i = p11; i <= p12; i++)
    {
        a1[j] = i;
        j++;
    }
    j = 0;
    for (int i = p21; i <= p22; i++)
    {
        a2[j] = i;
        j++;
    }
}

int test(int a1[], int a2[], int l1, int l2)
{
    for (int i = 0; i < l1; i++)
    {
        for (int j = 0; j < l2; j++)
        {
            if (a1[i] == a2[j])
            {
                return 1;
            }
        }
    }
    return 0;
}
