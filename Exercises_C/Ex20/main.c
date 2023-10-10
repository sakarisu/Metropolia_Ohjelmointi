#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "debug.h"

int main()
{
    srand(time(NULL));
    int debug_level;
    printf("Enter debug level (0-4): ");
    scanf("%d", &debug_level);
    set_debug_level(debug_level);
    for (int i = 1; i <= 5; i++)
    {
        int message_debug_level = rand() % 5;
        dprintf(message_debug_level, "Message %d with debug level %d\n", i, message_debug_level);
    }
    return 0;
}
