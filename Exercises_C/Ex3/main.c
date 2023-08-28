#include <stdio.h>

int students;
int i;
int student_number;
int grade;

int main()
{
    printf("How many students: ");      //Amount of students is given here
    scanf("%d", &students);
    int grades[students];
    for (i = 0; i < students; i++)
    {
        grades[i] = -1;
    }
    while (1)
    {       //Main loop
        printf("\nEnter student number (1 - %d) or 0 to stop: ", students);
        scanf("%d", &student_number);
        if (student_number == 0)
        {       //This stops the loop when 0 is entered when student number is asked
            break;
        }       //Invalid student numbers and grades are handled below
        if (student_number < 1 || student_number > students)
        {
            printf("Invalid student number!\n");
            continue;
        }
        printf("Enter grade (0 - 5) for student %d or -1 to cancel: ", student_number);
        scanf("%d", &grade);
        if (grade < -1 || grade > 5)
        {
            printf("Invalid grade! ");
            continue;
        }
        grades[student_number - 1] = grade;
    }       //Print student numbers and grades
    printf("\nStudent   Grade\n");
    for (i = 0; i < students; i++)
    {
        printf("%d\t", i + 1);
        if (grades[i] == -1)
        {
            printf("N/A\n");
        } else
        {
            printf("%3d\n", grades[i]);
        }
    }
    return 0;
}
