#include <stdio.h>
#include <stdlib.h>

#define MAX_ITEMS 40

typedef struct menu_item_
{
    char name[40];
    double price;
} menu_item;

int main()
{       //Main loop
    menu_item items[MAX_ITEMS];
    int item_count = 0;
    char filename[100];
    printf("Enter a filename: ");
    scanf("%s", filename);
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {       //If the fille is not found
        fprintf(stderr, "Error opening file: %s\n", filename);
        exit(1);
    }
    while (item_count < MAX_ITEMS && fscanf(file, "%[^;]; %lf\n", items[item_count].name, &items[item_count].price) == 2)
    {       //This loop reads the file for the item names and prices
        item_count++;
    }
    fclose(file);
    for (int i = 0; i < item_count; i++)
    {       //File gets printed here
        printf("%8.2f %s\n", items[i].price, items[i].name);
    }
    return 0;
}
