#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

#define MAX_WORD_LENGTH 32

bool password_generator(char* password, int size, const char* word) 
{
    int word_length = strlen(word);
    int password_length = word_length * 2 + 1;
    if (password_length >= size) 
    {
        return false;
    }
    srand(time(NULL));
    for (int i = 0; i < password_length; ++i) 
    {
        if (i % 2 == 0) 
        {
            password[i] = (rand() % (126 - 33 + 1)) + 33;
        } else 
        {
            password[i] = word[i / 2];
        }
    }
    password[password_length] = '\0';
    return true;
}

int main() 
{
    char word[MAX_WORD_LENGTH];
    char password[MAX_WORD_LENGTH * 2 + 1];
    bool stop = false;
    do 
    {
        printf("Enter a word or 'stop' to stop: ");
        fgets(word, sizeof(word), stdin);
        word[strcspn(word, "\n")] = '\0';
        if (strcmp(word, "stop") == 0) 
        {
            stop = true;
        } else if (password_generator(password, sizeof(password), word)) 
        {
            printf("Generated password: %s\n", password);
        } else 
        {
            printf("Error: Password does not fit in the string.\n");
        }
    } while (!stop);
    return 0;
}
