#include <stdio.h>
#include <string.h>

int string_length(char str[])
{       //Function that counts the length of the string in the array
    int count;
    for (count = 0; str[count] != '\0'; count++);
    return count;
}

int main()
{       //Main loop
    char str[1000];
    printf("Enter a string: ");
    fgets(str, 1000, stdin);
    while (strcmp(str, "stop\n") != 0)
    {       //Program stops when the user enter "stop"
        int length = string_length(str) - 1;
        printf("The string is: %s String length: %d\n", str, length);
        printf("Enter another string: ");
        fgets(str, 1000, stdin);
    }
    return 0;
}
