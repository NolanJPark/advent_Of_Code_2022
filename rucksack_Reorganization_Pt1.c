/*
A file contains a flurry of letters upper case and lower case letters in lines, and
you need to split the string on the line in half and find the common letter between
the two halves (case sensitive). Based on that letter you'll add points of priority
based on:
    a through z have priorities 1 through 26
    A through Z have priorities 27 through 52
*/

#include <stdio.h>
#include <ctype.h>

int main()
{
    //sum will hold the total priority of each line
    int sum = 0;
    //calls file
    FILE *fp = fopen("rucksack_Reorganization_File.txt", "r");
    //declares and initializes values, s is original line, s1 is first half, and s2 is latter half
    char s[200], s1[200], s2[200];
    //while loop that runs till end of file
    while (!feof(fp))
    {
        //scans line and stores it in s
        fscanf(fp, "%s\n", s);
        //calls fill
        fill(s, s1, s2);
        //calls prio and adds the return value to sum
        sum += prio(s1, s2);
    }
    //nicely prints out value of sum
    printf("Total priority sum is %d", sum);
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

void fill(char s[], char s1[], char s2[])
{
    //calls len and sets l to the return value
    int l = len(s);
    //runs half of l times
    for (int i = 0; i < l/2; i++)
    {
        s1[i] = s[i];
        //s2 starts halfway through s
        s2[i] = s[(l/2) + i];
    }
    //puts a null terminator at the end of s1 and s2 for saftey
    s1[l/2] = '\0';
    s2[l/2] = '\0';
}

int prio(char s1[], char s2[])
{
    //calls len and sets l to the return value
    int l = len(s1);
    //c will represent the common letter
    char c;
    //runs through s1 and s2
    for (int i = 0; i < l; i++)
    {
        for (int j = 0; j < l; j++)
        {
            //if a value at i in s1 and j in s2 is the same c is set to s1 at i and breaks the loop
            if (s1[i] == s2[j])
            {
                c = s1[i];
                break;
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
