#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_LINES 100
#define MAX_LINE_LENGTH 80

int main()
{       //Main loop
    char lines[MAX_LINES][MAX_LINE_LENGTH];
    int line_count = 0;
    char filename[100];
    printf("Enter a filename: ");
    scanf("%s", filename);
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {       //If the file is not found
        fprintf(stderr, "Error opening file: %s\n", filename);
        exit(1);
    }
    while (line_count < MAX_LINES && fgets(lines[line_count], MAX_LINE_LENGTH, file) != NULL)
    {       //This loop reads lines from the file
        line_count++;
    }
    fclose(file);
    for (int i = 0; i < line_count; i++)
    {       //Letters on the file are converted to upper case here
        for (int j = 0; lines[i][j] != '\0'; j++)
        {
            lines[i][j] = toupper(lines[i][j]);
        }
    }
    file = fopen(filename, "w");
    if (file == NULL)
    {       //If there is a problem opening the file again
        fprintf(stderr, "Error opening file: %s\n", filename);
        exit(1);
    }
    for (int i = 0; i < line_count; i++)
    {       //The file gets re-written here
        fputs(lines[i], file);
    }
    fclose(file);
    return 0;
}
