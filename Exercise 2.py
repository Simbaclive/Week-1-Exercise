using System;

class Program
{
    static void Main(string[] args)
    {
        // Ask the user for their grade percentage
        Console.Write("Enter your grade percentage: ");
        string input = Console.ReadLine();
        int grade = int.Parse(input);

        // Determine the letter grade
        string letter;

        if (grade >= 90)
        {
            letter = "A";
        }
        else if (grade >= 80)
        {
            letter = "B";
        }
        else if (grade >= 70)
        {
            letter = "C";
        }
        else if (grade >= 60)
        {
            letter = "D";
        }
        else
        {
            letter = "F";
        }

        // Determine the "+" or "-" sign for the letter grade
        string sign = "";
        if (letter != "F") // F grades don't have + or -
        {
            int lastDigit = grade % 10;

            if (lastDigit >= 7 && letter != "A") // "+" for 7-9 except A+
            {
                sign = "+";
            }
            else if (lastDigit < 3) // "-" for 0-2
            {
                sign = "-";
            }

            if (letter == "A" && lastDigit >= 7) // no A+
            {
                sign = "";
            }
        }

        // Print the final grade
        Console.WriteLine($"Your letter grade is: {letter}{sign}");

        // Check if the user passed
        if (grade >= 70)
        {
            Console.WriteLine("Congratulations, you passed the course!");
        }
        else
        {
            Console.WriteLine("Keep trying! You can improve next time.");
        }
    }
}
