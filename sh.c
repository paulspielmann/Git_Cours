#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define BUFFRER_SIZE 4096 // Standard unix shell buffer
#define PROMPT "> "

void process(char* foo);
void parseInput(char* foo, char** bar);

int main() {
    char* input = NULL;
    size_t input_size = 0;
    
    while (1) {
        printf(PROMPT);
        
        if (getline(&input, &input_size, stdin) == -1) {
            perror("Error reading input");
            free(input);
            exit(EXIT_FAILURE);
        }

        input[strcspn(input, "\n")] = '\0';

        char* tokens[BUFFRER_SIZE];
        parseInput(input, tokens);
    }

    free(input);
    return 0;
}

void process(char* input) {
    
    
    pid_t pid = fork();

    if (pid == 0) {
        execvp(command, args);
        perror("Erorr executing command");
        exit(EXIT_FAILURE);
    } else if (pid > 0) {
        perror("Forking error");
    } else {
        // Wait for parent process
        waitpid(pid, NULL, 0);
    }
}

// Separates input string into substrings delimited by spaces 
void parseInput(char* input, char* tokens[]) {
    int i = 0;
    char* token = strtok(input, " ");

    while (token != NULL) {
        tokens[i++] = token;
        token = strtok(NULL, " ");
    }

    tokens[i] = NULL;
}