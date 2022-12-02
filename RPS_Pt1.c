/*
A file contains a set of letters representing rock paper and scissors

Elf Moves:
A(65): Rock
B(66): Paper
C(67): Scissors

Your Moves:
X(88): Rock
Y(89): Paper
Z(90): Scissors

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
Your goal is to use the file with each round to determine how many points you'll get
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
int round(char elf, char you);

int main()
{
    //text file opened
    FILE *fp = fopen("RPS_File.txt", "r");
    //char that'll hold the elves move
    char elf;
    //char that'll hold your move
    char you;
    //int that'll hold the total value from this strategy
    int tot;
    //int that represent the round number
    int i = 0;
    //while loop that runs through whole file
    while (!feof(fp))
    {
        i++;
        //scans a line from the file and sets elf and you to values from the file
        fscanf(fp, "%c %c\n", &elf, &you);
        //calls round and sets the returned value to r
        int r = round(elf, you);
        //prints out round and value from round
        printf("round %d: %d\n", i, r);
        //adds round number to total
        tot += r;
    }
    //prints out total points
    printf("With the strategy the elves gave you you'll get %d points\n", tot);
    //closes file
    fclose(fp);
}

int round(char elf, char you)
{
    //sets elf and you char to integer values
    int e = (int)(elf);
    int y = (int)(you);
    //sets pts to 0
    int pts = 0;
    //if your choice is rock it adds one point, if it's paper two points are added, and if it's scissors 3 points are added
    if (y == X)//Rock
        pts++;
    else if (y == Y)//Paper
        pts += 2;
    else if (y == Z)//Scissors
        pts += 3;
    //if you won 6 points will be added and if it's a draw 3 points will be added, if you lose no points need to be added
    if ( (e == A && y == Y) || (e == B && y == Z) || (e == C && y == X) )//win
        pts += 6;
    else if ( (e == A && y == X) || (e == B && y == Y) || (e == C && y == Z) )//draw
        pts += 3;
    return pts;
}
