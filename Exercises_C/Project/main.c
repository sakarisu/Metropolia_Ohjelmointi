#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE_LENGTH 100
#define MAX_NUM_ENTRIES 50
#define MAX_DAY_LENGTH 10
#define MAX_TIME_LENGTH 6
#define MAX_COURSE_LENGTH 100
#define MAX_ROOM_LENGTH 10

typedef struct
{       //Structure of how the CSV-file is read
    char day[MAX_DAY_LENGTH];
    char time[MAX_TIME_LENGTH];
    char course[MAX_COURSE_LENGTH];
    char room[MAX_ROOM_LENGTH];
} Schedule;

int compare(const void *a, const void *b)
{       //Function for determining the order of elements in an array
    Schedule *scheduleA = (Schedule *)a;
    Schedule *scheduleB = (Schedule *)b;
    return strcmp(scheduleA->time, scheduleB->time);
}

void toLowerCase(char *str)
{       //Function for making user input case insensitive
    for(int i = 0; str[i]; i++){
        str[i] = tolower(str[i]);
    }
}

int main()
{
    FILE *file = fopen("schedule.csv", "r");
    if (file == NULL)
    {       //If the schedule.csv file is not found
        printf("Could not open file\n");
        return 1;
    }
    Schedule schedules[MAX_NUM_ENTRIES];
    int numEntries = 0;
    char line[MAX_LINE_LENGTH];
    fgets(line, sizeof(line), file);
    while (fgets(line, sizeof(line), file))
    {       //The file is read here
        sscanf(line, "%[^,],%[^,],%[^,],%[^\n]", schedules[numEntries].day, schedules[numEntries].time,
               schedules[numEntries].course, schedules[numEntries].room);
        toLowerCase(schedules[numEntries].day);
        numEntries++;
    }
    fclose(file);
    while (1)
    {       //Main loop
        printf("Enter day: ");
        char day[MAX_DAY_LENGTH];
        fgets(day, sizeof(day), stdin);
        day[strcspn(day, "\n")] = 0;
        toLowerCase(day);
        if (strcmp(day, "stop") == 0)
        {       //For when the user wants to stop the program
            break;
        }
        Schedule daySchedules[MAX_NUM_ENTRIES];
        int numDaySchedules = 0;
        for (int i = 0; i < numEntries; i++)
        {       //The correct schedule info for the day the user entered gets collected here
            if (strcmp(schedules[i].day, day) == 0)
            {       //If the day matches user input
                daySchedules[numDaySchedules] = schedules[i];
                numDaySchedules++;
            }
        }
        if (numDaySchedules == 0)
        {       //If the day contains no info (classes)
            printf("No classes today\n");
            continue;
        }
        qsort(daySchedules, numDaySchedules, sizeof(Schedule), compare);
        printf("On %s you have:\n", day);
        for (int i = 0; i < numDaySchedules; i++)
        {       //Schedule gets printed here
            printf("%s %s, %s\n", daySchedules[i].time, daySchedules[i].course, daySchedules[i].room);
        }
    }
    return 0;
}
