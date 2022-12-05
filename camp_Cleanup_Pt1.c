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
        if (p11 >= p21 && p12 <= p22)
            tot++;
        else if (p21 >= p11 && p22 <= p12)
            tot++;
    }
    printf("In %d assignment pairs one range fully contains the other", tot);
    fclose(fp);
}
