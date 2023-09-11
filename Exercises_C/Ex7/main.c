#include <stdio.h>
#include <stdbool.h>

bool read_positive(int *value)
{       //Function that reads the input and returns a boolean value
    int i;
    printf("Enter a positive number: \n");
    if (scanf("%d", &i) == 1 && i > 0)
    {
        *value = i;
        return true;
    }
    return false;
}

int main()
{       //Main loop
    int guess = 0;
    int incorrects = 0;
    int money;
    while (incorrects < 3)
    {
        printf("Guess how much money I have!\n");
        if (read_positive(&guess))
        {       //If the input is a positive number
            money = guess * 2 + 20;
            printf("You didn't guess right. I have %d euros.\n", money);
        } else
        {       //If the input is invalid (negative number or a letter)
            incorrects ++;
            printf("Incorrect input\n");
            while (getchar() != '\n');
        }
    }
    printf("I give up! See you later!");
    return 0;
}
