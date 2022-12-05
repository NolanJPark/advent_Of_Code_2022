/*
File supply_Stacks_File.txt contains stacks of characters and below it a list of all the actions
that a crane will be taking. The crane moves whole stacks at once instead of one at a time
*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
public class supply_Stacks_Pt2
{
    public static void main(String[] args)
    {
        try
        {
            File f = new File("supply_Stacks_File.txt");
            Scanner r = new Scanner(f);
            stacks a[] = new stacks[9];
            a[0] = new stacks();
            a[1] = new stacks();
            a[2] = new stacks();
            a[3] = new stacks();
            a[4] = new stacks();
            a[5] = new stacks();
            a[6] = new stacks();
            a[7] = new stacks();
            a[8] = new stacks();
            for (int l = 0; l < 8; l++)
            {
                String s = r.nextLine();
                for (int i = 0; i < 9; i++)
                {
                    char c = s.charAt(1+i*4);
                    if ((int)c != 32)
                    {
                        a[i].enter(s.substring(1+i*4, 2+i*4));
                    }
                }
            }
            print(a);
            r.nextLine();
            r.nextLine();
            while (r.hasNextLine())
            {
                String s = r.nextLine();
                int t = getInt(s, 1);
                int p1 = getInt(s, 3) - 1;
                int p2 = getInt(s, 5) - 1;
                for (int j = 0; j < t; j++)
                {
                    //difference between Pt1 and Pt2 is Pt1 uses removeTop and Pt2 uses removePart
                    String temp = a[p1].removePart(t - j);
                    a[p2].putOnTop(temp);
                }
            }
            System.out.println("\n");
            print(a);
            System.out.print("The top layer is: "+topLayer(a));
            r.close();
        }
        catch (FileNotFoundException e)
        {
            System.out.println("wtf something went wrong getting the file");
            e.printStackTrace();
        }
    }
    
    /*
     * Prints out the stacks in horizontal format using the stacks array and the output function in the stacks class
     */
    public static void print(stacks a[])
    {
        for (int i = 0; i < 9; i++)
        {
            System.out.print((i+1)+") ");
            a[i].output();
            System.out.println();
        }
    }
    
    /*
     * Function takes a string and an integer that represents which number in the string you want to get.
     * Since the file's instructions are formatted in a consistant way x is used as an easier way to find the desired number,
     * and returns the desired number from the string.
     */
    public static int getInt(String s, int x)
    {
        for (int i = 0; i < x; i++)
        {
            int y = s.indexOf(' ');
            s = s.substring(y+1);
        }
        int y = s.indexOf(' ');
        if (y != -1)
        {
            y = s.indexOf(' ');
            s = s.substring(0, y);
        }
        return Integer.parseInt(s);
    }
    
    /*
     * Takes an array of stacks as a parameter and uses the getTop function from the stacks class to return a string
     * that has the character at the top of the stacks in order from 1 to 9
     */
    public static String topLayer(stacks a[])
    {
        String s = "";
        for (int i = 0; i < a.length; i++)
        {
            s += a[i].getTop();
        }
        return s;
    }
}
