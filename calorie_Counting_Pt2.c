/*
Same as part 1 but now you need to find the total of the top 3 groups
*/
#include <stdio.h>

int main()
{
    //temp will hold each group's calories before comparing it to the largest calorie holder
    int temp = 0;
    //first row will hold the group number and second row will hold that groups total calories
    int max[2][3] = {0,0,0,0,0,0};
    //buffer for input from file, it's a string so it can be tested for if it's a blank line
    char buf[BUFSIZ];
    //calls file
    FILE *fp = fopen("calorie_Counting_File.txt", "r");
    //int for the group the loop is on
    int i = 0;
    while (!feof(fp))
    {
        //gets line in file as a string and stores it in buf
        fgets(buf, sizeof(buf), fp);
        //if statement that runs if the buffer is an empty line meaning the group has ended
        if (!strcmp(buf, "\n"))
        {
            //adds to group number
            i++;
            //runs if temp is greater than the current 1st greatest
            if (temp > max[1][0])
            {
                //makes 3rd equal to 2nd
                max[1][2] = max[1][1];
                max[0][2] = max[0][1];
                //makes 2nd equal to 1st
                max[1][1] = max[1][0];
                max[0][1] = max[0][0];
                //sets 1st to temp and temps group number
                max[1][0] = temp;
                max[0][0] = i;
            }
            //runs if temp is greater than the 2nd greatest
            else if (temp > max[1][1])
            {
                //makes 3rd equal to 2nd
                max[1][2] = max[1][1];
                max[0][2] = max[0][1];
                //sets 2nd to temp and temps group number
                max[1][1] = temp;
                max[0][1] = i;
            }
            //runs if temp is greater than the 3rd greatest
            else if (temp > max[1][2])
            {
                //sets 3rd to temp and temps group number
                max[1][2] = temp;
                max[0][2] = i;
            }
            //resets temp
            temp = 0;
        }
        //if buffer isn't an empty line it's converted to an int and added to temp
        else
        {
            temp += atoi(buf);
        }
    }
    //tot is equal to 1st, 2nd, and 3rd greatest calorie holding groups
    int tot = max[1][0] + max[1][1] + max[1][2];
    //prints it all nicely
    printf("1.) %d group %d\n", max[1][0], max[0][0]);
    printf("2.) %d group %d\n", max[1][1], max[0][1]);
    printf("3.) %d group %d\n", max[1][2], max[0][2]);
    printf("Total calories: %d", tot);
}
