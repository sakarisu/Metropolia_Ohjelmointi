#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main()
{       //Main loop
    char filename[100];
    printf("Enter a filename: ");       //User needs to enter the full file name (hello.txt, not just hello)
    scanf("%s", filename);
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {       //If the file is not found
        fprintf(stderr, "Error opening file: %s\n", filename);
        exit(1);
    }
    int num, count = 0, min = INT_MAX, max = INT_MIN;
    while (fscanf(file, "%d", &num) == 1)
    {       //Lowest and highest numbers are set here
        count++;
        if (num < min) min = num;
        if (num > max) max = num;
    }
    printf("Count of numbers: %d\n", count);
    printf("Lowest number: %d\n", min);
    printf("Highest number: %d\n", max);
    fclose(file);
    return 0;
}
