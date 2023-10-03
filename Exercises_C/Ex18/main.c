#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(NULL));
    int shift_amount = 0;
    do
    {
        printf("Enter a number in the range from 0 to 15 or a negative number to stop: ");
        scanf("%d", &shift_amount);
        if(shift_amount >= 0 && shift_amount <= 15)
        {
            int num = rand();
            printf("Generated number: %x\n", num);
            int result = (num >> shift_amount) & 0x3F;
            printf("Result: %02x\n", result);
        } else if(shift_amount > 15)
        {
            printf("Invalid input! Please enter a number in the range from 0 to 15 or a negative number to stop.\n");
        }
    } while(shift_amount >= 0);
    return 0;
}
