import java.util.*;

class Time_Workings
{
    int hr,min,sec;
    Time_Workings()
    {
        hr = 0;
        min = 0;
        sec = 0;
    }
    Time_Workings(int hr, int min, int sec)
    {
        this.hr = hr;
        this.min = min;
        this.sec = sec;
    }
    void display()
    {
        System.out.println("Time is 12 Hour Format ");
        if(hr <= 12)
        {
            System.out.println(hr + " : " + min + " : " + sec + " AM");
        }
        else
        {
            System.out.println((hr - 12) + " : " + min + " : " + sec + " PM");
        }
    }
}

class Time
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Time in 24 Hour Format ");
        System.out.print("Enter hr : ");
        int x = sc.nextInt();
        System.out.print("Enter min : ");
        int y = sc.nextInt();
        System.out.print("Enter sec : ");
        int z = sc.nextInt();

        if(x > 24)
        {
            System.out.println("Invalid Input");
            System.exit(0);
        }
        if(y > 60)
        {
            x = (x + (y / 60));
            if(x > 24)
            {
                x = (x - 24);
            }
            y = (y % 60);
        }
        if(z > 60)
        {
            y = (y + (z / 60));
            z = (z % 60);
        }

        Time_Workings t = new Time_Workings(x,y,z);
        t.display();
    }
}