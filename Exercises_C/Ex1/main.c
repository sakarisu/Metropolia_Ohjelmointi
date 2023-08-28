#include <stdio.h>

float bus_cost;
float taxi_cost;
float money;
int select;

int main()
{       //Variables are assigned here
    printf("Enter price of bus ticket: \n");
    scanf("%f", &bus_cost);
    printf("Enter price of taxi: \n");
    scanf("%f", &taxi_cost);
    printf("How much money you have: \n");
    scanf("%f", &money);
    if (money < 0 )         //This is here to make sure that you can't go into debt for transportation
    {
        money = 0;
    }
    do
    {       //Main loop
        printf("You have %.2f euros left.\n", money);
        printf("Do you want to take\n1) bus (%.2f euros)\n2) taxi (%.2f euros)\n", bus_cost, taxi_cost);
        printf("Enter your selection: \n");
        scanf("%d", &select);
        if (select == 1)
        {
            printf("You chose bus.\n");
            if (money < bus_cost)
            {
                printf("You don't have enough money for bus.\n");
            } else
            {
                money -= bus_cost;
                select = 0;
            }
        }
        if (select == 2)
        {
            printf("You chose taxi.\n");
            if (money < taxi_cost)
            {
                printf("You don't have enough money for taxi. \n");
            } else
            {
                money -= taxi_cost;
                select = 0;
            }
        }
    }
    while (money >= bus_cost || money >= taxi_cost);
    printf("You don't have enough money left for bus or taxi.\n");
    printf("You have to walk.\n");
    return 0;
}
