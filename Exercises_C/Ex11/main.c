#include <stdio.h>

int replace_char(char *str, const char *repl)
{       //Function that changes a character from a string to another
    int count = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == repl[0])
        {
            str[i] = repl[1];
            count++;
        }
    }
    return count;
}

int main()
{       //Main loop
    char str[1000];
    char repl[3];
    int count;
    printf("Enter a string: \n");
    fgets(str, 1000, stdin);
    printf("Enter a character and what you would like to replace it with: \n");
    fgets(repl, 3, stdin);
    count = replace_char(str, repl);
    if (count > 0)
    {       //Inputs for string and new character
        printf("The new string: %s", str);
        printf("Amount of changed characters: %d\n", count);
    }
    else
    {       //If nothing is changed, program goes here
        printf("String wasn't changed.\n");
    }
    return 0;
}
