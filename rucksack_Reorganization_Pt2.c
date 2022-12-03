/*
This time you need to sort 3 lines into a group and then find the common letter
among those three lines. Then you need to find the priority and add it all together.
*/
#include <stdio.h>
#include <ctype.h>

int main()
{
    //sum will hold the total priority of each line
    int sum = 0;
    //calls file
    FILE *fp = fopen("rucksack_Reorganization_File.txt", "r");
    //declares and initializes values, s1 is the first line, s2 is the second line, and s3 is the 3rd line
    char s1[200], s2[200], s3[200];
    //while loop that runs till end of file
    while (!feof(fp))
    {
        //scans three lines and sets the strings to the lines
        fscanf(fp, "%s\n", s1);
        fscanf(fp, "%s\n", s2);
        fscanf(fp, "%s\n", s3);
        //calls prio and adds the return value to sum
        sum += prio(s1,s2,s3);
    }
    //nicely prints out value of sum
    printf("Total group priority sum is %d", sum);
    //closes file
    fclose(fp);
}

int len(char s[])
{
    //i represents length of string
    int i = 0;
    //runs till it runs into the index with the null terminator
    while (s[i] != '\0')
        i++;
    //returns i
    return i;
}

int prio(char s1[], char s2[], char s3[])
{
    //calls len for each string and sets them respectively
    int L1 = len(s1);
    int L2 = len(s2);
    int L3 = len(s3);
    //c will represent the common letter
    char c;
    //runs through s1, s2, and s3
    for (int i = 0; i < L1; i++)
    {
        for (int j = 0; j < L2; j++)
        {
            for (int k = 0; k < L3; k++)
            {
                //if a value at i in s1 and j in s2 is the same a value at j in s2 and k in s3 and c is set to s1 at i and breaks the loop
                if (s1[i] == s2[j] && s2[j] == s3[k])
                {
                    c = s1[i];
                    break;
                }

            }
        }
    }
    //runs statement based on whether c is upper or lower case
    if (islower(c))
        return (int)(c) - 96; //subtracts 96 from int value of c based on ascii table
    else if (isupper(c))
        return (int)(c) - 38; //subtracts 38 from int value of c based on ascii table
    return 0;
}
