#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int roll_dice(int sides)
{
    return rand() % sides + 1;
}

int read_range(int low, int high)
{
    int i;
    while (1)
    {
        printf("Enter a number between %d and %d: ", low, high);
        scanf("%d", &i);
        if (i >= low && i <= high)
        {
            return i;
        }
        printf("Invalid input. ");
        while (getchar() != '\n');
    }
}

int main() {
    srand(time(NULL));
    printf("Welcome to the dice game!\n");
    while (1)
    {
        printf("Select an operation:\n");
        printf("1. Roll D6\n");
        printf("2. Roll D10\n");
        printf("3. Quit\n");
        int choice = read_range(1, 3);
        if (choice == 1)
        {
            printf("You rolled a %d.\n", roll_dice(6));
        } else if (choice == 2)
        {
            printf("You rolled a %d.\n", roll_dice(10));
        } else
        {
            printf("Goodbye!\n");
            break;
        }
    }
    return 0;
}
