#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    int number;
    struct node *next;
} nnode;

int main()
{
    char input[1000];
    nnode *head = NULL, *temp = NULL;
    int end = 0;
    do
    {
        printf("Enter a number or 'end' to stop: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0;
        if(strcmp(input, "end") == 0)
        {
            end = 1;
            continue;
        }
        int num;
        if(sscanf(input, "%d", &num) != 1)
        {
            printf("Invalid input! Please enter a number or 'end'.\n");
            continue;
        }
        nnode *new_node = (nnode*)malloc(sizeof(nnode));
        new_node->number = num;
        new_node->next = NULL;
        if(head == NULL)
        {
            head = new_node;
            temp = new_node;
        } else
        {
            temp->next = new_node;
            temp = new_node;
        }
    } while(!end);
    printf("Entered numbers: ");
    temp = head;
    while(temp != NULL)
    {
        printf("%d ", temp->number);
        nnode *old_temp = temp;
        temp = temp->next;
        free(old_temp);
    }
    printf("\n");
    return 0;
}
