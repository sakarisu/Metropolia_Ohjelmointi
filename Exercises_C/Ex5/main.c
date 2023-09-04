#include <stdio.h>

int read_range(int low, int high) {
    int i;
    while (1)
    {
        printf("Roll a die and enter your result.\nEnter a number between %d and %d: ", low, high);
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
    printf("Let's play!\n");
    for (int i = 0; i < 3; i++)
    {
        int user_roll = read_range(1, 6);
        int prog_roll = user_roll == 6 ? 6 : user_roll + 1;
        printf("I got %d. ", prog_roll);
        if (prog_roll > user_roll)
        {
            printf("I win!\n");
        } else if (prog_roll == user_roll)
        {
            printf("It's a tie!\n");
        } else
        {
            printf("You win!\n");
        }
    }
    printf("Better luck next time. Bye!\n");
    return 0;
}
