#include <stdio.h>
#include <string.h>

int count_words(const char* str, const char *word)
{       //Function that counts how many times a word appears in a string
    int count = 0;
    const char *counter = str;

    while ((counter = strstr(counter, word)) != NULL)
    {
        count++;
        counter += strlen(word);
    }
    return count;
}


int main()
{       //Main loop
    char str[1000];
    char word[1000];
    int count;
    int stop = 0;       //Int stop is here to avoid having to use break to end the loop

    while (!stop)
    {       //Inputs for string and the word that is to be counted
        printf("Enter a string: ");
        fgets(str, 1000, stdin);
        printf("Enter a word: ");
        fgets(word, 1000, stdin);
        str[strcspn(str, "\n")] = '\0';
        word[strcspn(word, "\n")] = '\0';
        if (strcmp(str, "stop") == 0 || strcmp(word, "stop") == 0)
            stop = 1;
        else
        {       //Print is here
            count = count_words(str, word);
            printf("The word \"%s\" occurs %d times in \"%s\".\n", word, count, str);
        }
    }

    return 0;
}
