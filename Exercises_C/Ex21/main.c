#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned char calculate_checksum(const char *s) 
{
    unsigned char checksum = 0;
    while (*s) 
    {
        checksum ^= *s;
        s++;
    }
    return checksum;
}

int main() 
{
    char filename[100];
    printf("Enter a filename: ");
    scanf("%s", filename);
    FILE *file = fopen(filename, "r");
    if (file == NULL) 
    {
        fprintf(stderr, "Error opening file: %s\n", filename);
        return 1;
    }
    char line[1024];
    while (fgets(line, sizeof(line), file)) 
    {
        char *start = strchr(line, '$');
        char *end = strchr(line, '*');
        if (start != NULL && end != NULL && start < end) 
        {
            unsigned char checksum = calculate_checksum(start + 1);
            unsigned int file_checksum;
            sscanf(end + 1, "%2x", &file_checksum);
            if (checksum == file_checksum) 
            {
                printf("[ OK ] %s", line);
            } else 
            {
                printf("[FAIL] %s", line);
            }
        }
    }
    fclose(file);
    return 0;
}
