# Python Basic Coding

## Printing Prime numbers

This script efficiently prints all prime numbers up to a given number $n$. A prime number is defined as an integer greater than 1 that has no divisors other than 1 and itself. The script uses a helper function, `is_prime()`, to check if a number is prime by testing divisibility up to its square root. The main function, `print_primes(n)`, generates a list of all prime numbers from 2 to $n$ and prints them in a clean, readable format. This approach ensures simplicity and clarity, making it easy to modify for different ranges or use cases. For example, calling the function with $n = 50$ will output all prime numbers between 2 and 50.

## Printing Odd Numbers & Even Numbers

-   **Odd Numbers:** if the number not exactly divisible by 2 , then it called odd number
-   **Even Numbers:** if the number exactly dividible by 2 , then it called Even Number

## Checking panrindrome

A **palindrome** is a word, phrase, number, or sequence of characters that reads the same backward as forward, ignoring spaces, punctuation, and capitalization. For example, the words "madam", "radar", and the number 121 are palindromes. Palindromes are often used in puzzles and word games due to their symmetry and unique properties. In programming, palindromes are commonly identified by checking if the original string or number is equal to its reverse.

## Factors & It's Occurances

To find the **factors** of a number and their **occurrences**, you essentially break the number into its prime factors and determine how many times each prime factor occurs in its decomposition.

### Steps:

1.  **Find the Prime Factors**: Break down the number into its prime components.

2.  **Count Occurrences**: For each prime factor, count how many times it divides the number.

## Printing Calendar
In Python, printing a calendar can be easily achieved using the built-in calendar module, which provides functions to work with dates and calendars. The module allows you to display a monthly or yearly calendar in a text format. For example, the calendar.month() function prints the calendar for a specific month, while calendar.calendar() displays the calendar for an entire year. The output is neatly formatted to show the days of the week and the corresponding dates. The module also offers customization options, such as setting the first day of the week to Monday or Sunday. This makes the calendar module a convenient tool for date-related programming tasks, such as scheduling or date visualization. 

## Fibonacci Sequences 

The **Fibonacci sequence** is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. The sequence begins as \( 0, 1, 1, 2, 3, 5, 8, 13, 21, \dots \), where each term is calculated as \( F(n) = F(n-1) + F(n-2) \). It is named after the Italian mathematician Leonardo of Pisa, known as Fibonacci, who introduced the sequence to the Western world in his book *Liber Abaci*. The Fibonacci sequence has widespread applications in mathematics, computer science, and nature, appearing in phenomena such as the arrangement of leaves on a stem, the branching of trees, and the spiral patterns of shells. It also serves as a foundation for solving problems in dynamic programming and recursion in computer science. In Python, the Fibonacci sequence can be generated using a loop, recursion, or dynamic programming techniques.

## Counting The Unqiue letters Occurances

Counting the unique letter occurrences in a string involves identifying each distinct character and determining how many times it appears. This process helps analyze text for frequency distribution, detect patterns, or preprocess data for tasks like text mining or cryptography. In Python, this can be efficiently achieved using a dictionary or the `collections.Counter` module, which maps each unique letter to its corresponding count. The approach typically involves iterating through the string, ignoring spaces and punctuation if necessary, and updating the count for each letter. For example, in the string *"hello world"*, the unique letters are *h, e, l, o, r, d, w*, with their respective counts being 1, 1, 3, 2, 1, 1, 1. This technique is commonly used in data analysis and natural language processing to understand text characteristics.
