/*
A file contains a set of letters representing rock paper and scissors

Elf Moves:
A(65): Rock
B(66): Paper
C(67): Scissors

Your Moves:
X(88): You Need to Lose
Y(89): You Need a Draw
Z(90): You Need to Win

You gets points depending on how each round goes, your score is the sum of the points based on
your choice, and the outcome of the round.
Points:
    >1 for rock
    >2 for paper
    >3 for scissors
    +
    >0 if you lose
    >3 if it's a draw
    >6 if you win
This time around X Y and Z represents how the round needs to go, otherwise everything is the same
and you need to find the total points the elf's strategy would get you
*/

#include <stdio.h>
//Symbolic Constants that represent each letter for convinience
#define A 65
#define B 66
#define C 67
#define X 88
#define Y 89
#define Z 90

//prototype cause C
int round(char elf, char end);

int main()
{
    //text file opened
    FILE *fp = fopen("RPS_File.txt", "r");
    //char that'll hold the elves move
    char elf;
    //char that'll hold whether you need to win, draw, or lose
    char end;
    //int that'll hold the total value from this strategy
    int tot = 0;
    //int that represent the round number
    int i = 0;
    //while loop that runs through whole file
    while (!feof(fp))
    {
        i++;
        //scans a line from the file and sets elf and you to values from the file
        fscanf(fp, "%c %c\n", &elf, &end);
        //calls round and sets the returned value to r
        int r  = round(elf, end);
        //prints out round and value from round
        printf("round %d) %d\n", i, r, elf, end);
        //adds round number to total
        tot += r;
    }
    //prints out total points
    printf("With the strategy the elves gave you you'll get %d points\n", tot);
    //closes file
    fclose(fp);
}

int round(char elf, char end)
{
    //sets elf and end char to integer values
    int el = (int)(elf);
    int en = (int)(end);
    //sets pts to 0
    int pts = 0;
    //runs a if statement depending on whether you need to win, lose, or have a draw
    if (en == Y)//draw
    {
        //determines what you'll need for the desired outcome and adds points based on that
        if (el == A)//el = rock
            pts++;
        else if (el == B)//el = paper
            pts += 2;
        else//el = scissors
            pts += 3;
        //adds 3 points since you had a draw
        pts += 3;
    }
    else if (en == Z)//win
    {
        //determines what you'll need for the desired outcome and adds points based on that
        if (el == A)//el = rock
            pts += 2;
        else if (el == B)//el = paper
            pts += 3;
        else//el = scissors
            pts++;
        //adds 6 points since you won
        pts += 6;
    }
    else//loss
    {
        //determines what you'll need for the desired outcome and adds points based on that
        if (el == A)//el = rock
            pts += 3;
        else if (el == B)//el = paper
            pts++;
        else//el = scissors
            pts += 2;
        //adds no points since you lost
    }
    return pts;
}
