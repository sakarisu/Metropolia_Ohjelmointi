#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void print_numbers(const int *array, int count)
{       //Function for printing an array of numbers
    int i;
    for (i = 0; i < count; i++)
    {
        printf("%8d\n", array[i]);
    }
}

int main()
{       //Main loop that adds 15 random numbers to an array and prints them all line by line
    int numbers[15];
    srand(time(NULL));
    for (int i = 0; i < 15; i++)
    {
        numbers[i] = rand() % 100;
    }
    print_numbers(numbers, 15);
    return 0;
}
