#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ITEMS 40

typedef struct menu_item_
{
    char name[40];
    double price;
} menu_item;

int compare_by_name(const void *a, const void *b)
{       //Function for sorting by name
    menu_item *itemA = (menu_item *)a;
    menu_item *itemB = (menu_item *)b;
    return strcmp(itemA->name, itemB->name);
}
int compare_by_price(const void *a, const void *b)
{       //Function for sorting by price
    menu_item *itemA = (menu_item *)a;
    menu_item *itemB = (menu_item *)b;
    if (itemA->price < itemB->price) return -1;
    else if (itemA->price > itemB->price) return 1;
    else return 0;
}

int main()
{       //Main loop
    menu_item items[MAX_ITEMS];
    int item_count = 0;
    char filename[100];
    printf("Enter a filename: ");
    scanf("%s", filename);
    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {       //If the file is not found
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
    printf("Choose sorting order: (1) by name, (2) by price: ");
    int choice;
    scanf("%d", &choice);
    if (choice == 1)        //Sort by name
        qsort(items, item_count, sizeof(menu_item), compare_by_name);
    else if (choice == 2)       //Sort by price
        qsort(items, item_count, sizeof(menu_item), compare_by_price);
    for (int i = 0; i < item_count; i++)
        printf("%8.2f %s\n", items[i].price, items[i].name);
    return 0;
}
