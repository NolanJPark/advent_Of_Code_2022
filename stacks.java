import java.util.*;
import java.io.File;
public class stacks
{
    //field a is an arraylist holding the characters within a stack as Strings
    private ArrayList<String> a;
    //stacks constructor initializes a
    public stacks()
    {
        a = new ArrayList<String>();
    }
    //enter method takes a string and adds it to the beginning of a
    public void enter(String s)
    {
        a.add(0, s);
    }
    //output method prints out all the characters in a in a straight line
    public void output()
    {
        for (int i = 0; i < a.size(); i++)
            System.out.print(a.get(i)+" ");
    }
    //removeTop method removes the string from the end of the arraylist and returns it
    public String removeTop()
    {
        return a.remove(a.size() - 1);
    }
    //putOnTop method takes a string parameter and adds it on the end of the arraylist
    public void putOnTop(String s)
    {
        a.add(s);
    }
    //getTop method gets the string at the end of the arraylist
    public String getTop()
    {
        return a.get(a.size() - 1);
    }
    //remoePart method removes a string x away from te string at the end of the arraylist
    public String removePart(int x)
    {
        return a.remove(a.size() - x); 
    }
}
