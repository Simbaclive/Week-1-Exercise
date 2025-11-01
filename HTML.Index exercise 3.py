using System;

class Program
{
    static void Main(string[] args)
    {
        string playAgain;

        do
        {
            // Generate a random number between 1 and 100
            Random randomGenerator = new Random();
            int magicNumber = randomGenerator.Next(1, 101);

            int guess = 0;
            int guessCount = 0;

            Console.WriteLine("I have picked a magic number between 1 and 100. Can you guess it?");

            // Loop until the user guesses correctly
            while (guess != magicNumber)
            {
                Console.Write("Enter your guess: ");
                string input = Console.ReadLine();
