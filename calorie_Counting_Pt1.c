/*
A file contains a list of numbers, blank lines seperate each group, and
you need to find the group with the largest total number after adding
up the individual numbers in the group.
*/

#include <stdio.h>

int main()
{
    //temp will hold each group's calories before comparing it to the largest calorie holder
    int temp = 0;
    //max is the largest calorie holder
    int max = 0;
    //elf is just a holder for the group number with the most calories
    int elf;
    //buffer for input from file, it's a string so it can be tested for if it's a blank line
    char buf[BUFSIZ];
    //calls file
    FILE *fp = fopen("calorie_Counting_File.txt", "r");
    //int for the group the loop is on
    int i = 0;
    //while loop that runs till end of file
    while (!feof(fp))
    {
        //gets line in file as a string and stores it in buf
        fgets(buf, sizeof(buf), fp);
        //if statement that runs if the buffer is an empty line meaning the group has ended
        if (!strcmp(buf, "\n"))
        {
            //adds to i
            i++;
            //runs if temp is greater than max
            if (temp > max)
            {
                .//max is set to temp and elf is set to i
                max = temp;
                elf = i;
            }
            //temp is reset to 0
            temp = 0;
        }
        //if buffer isn't an empty line it's converted to an int and added to temp
        else
        {
            temp += atoi(buf);
        }
    }
    //prints out elf group with the most calories and the amount they have
    printf("Elf group %d has the most with %d total calories", elf, max);
}
