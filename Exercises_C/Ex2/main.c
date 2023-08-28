#include <stdio.h>

float tax[12];      //Arrays etc. are defined here
float income[12];
int sum;        //Sum of the incomes, required for applying the new tax rate
float tax_rate;
float income_limit;
float big_tax;      //New tax rate over income limit

int main()
{
    int i;
    printf("Enter tax rate: \n");       //Tax rate etc are entered here
    scanf("%f", &tax_rate);
    printf("Enter income limit: \n");
    scanf("%f", &income_limit);
    printf("Enter tax rate over income limit: \n");
    scanf("%f", &big_tax);
    for (int i = 0; i < 12; i++)        //Monthly income is entered and calculated in this loop
    {
        printf("Enter income for month %d: \n", i + 1);
        scanf("%f", &income[i]);
        tax[i] = income[i] * tax_rate / 100;        //Tax is calculated here
        sum += income[i];
        if (sum >= income_limit)        //Tax rate over income limit is applied here
        {
            tax[i] = income[i] * big_tax / 100;
        }
    }
    printf(" Month      Income        Tax\n");
    for (int i = 0; i < 12; i++)        //Income and taxes are printed here
    {
        printf("%6d  %10.2f %10.2f\n", i + 1, income[i], tax[i]);
    }
    return 0;
}
