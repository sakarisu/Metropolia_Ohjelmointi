#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int find_first(const unsigned int *array, unsigned int what)
{       //Function for finding the numbers in an array
    for (int i = 0; i < 20; i++)
    {
        if (array[i] == what)
        {
            return i;
        }
        if (array[i] == 0)
        {
            return -1;
        }
    }
    return -1;
}

int main(void)
{
    int array[20];
    srand(time(NULL));
    printf("The array is: \n");
    for (int i = 0; i < 20; i++)
    {       //Add random numbers to array
        array[i] = rand() % 20 + 1;
        printf("%u\n", array[i]);
    }
    int input;
    printf("Enter a number to search for or zero to stop: ");
    scanf("%u", &input);        //The user is asked to enter numbers here
    while (input != 0)
    {       //While-loop for finding the numbers in the array (program stops when 0 is entered)
        int result = find_first(array, input);
        if (result != -1)
        {
            printf("The number %u is found at index %d.\n", input, result + 1);
        }
        else
        {
            printf("The number %u is not found.\n", input);
        }
        printf("Enter another number to search for or zero to stop: ");
        scanf("%u", &input);
    }
    printf("Goodbye!\n");
    return 0;
}
