#include <stdio.h>

int i, n = 0, sum = 0;
float average;

int read_integer(void)
{       //Function that reads a single integer
    if (scanf("%d", &i) == 1)
    {
        return i;
    }       //If anything other than a number is entered
    n --;       //Makes sure only numbers get added to the count
    printf("Invalid input.\n");
    while (getchar() != '\n');
};

int main()
{       //Main loop
    printf("Enter positive number or negative to stop: \n");
    while ((i = read_integer()) >= 0)
    {       //Loop for reading user inputs until a negative number is entered
        n ++;
        sum += i;
        printf("Enter positive number or negative to stop: \n");
    };
    if (n > 0)
    {       //Amount of numbers and average is printed here
        average = (float)sum / n;
        printf("You entered %d positive numbers. The average is: %.3f.", n, average);
    }
    return 0;
}
