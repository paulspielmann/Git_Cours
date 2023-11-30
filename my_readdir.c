#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

#define INITIAL_CAPACITY 10
#define MAX_FILENAME_LENGTH 255 // On ext filesystems (most unix systems)

char** my_readdir(char *path) {
    char **res = NULL;
    int dir_fd;
    // Fail on trying to open non directory
    if ((dir_fd = open(path, O_RDONLY, O_DIRECTORY)) == -1) {
        perror("open error");
        exit(EXIT_FAILURE);
    }

    struct {
        off_t dir_offset;
        unsigned short dir_length;
        char dir_name[MAX_FILENAME_LENGTH];
    } dir_buffer;

    size_t capacity = INITIAL_CAPACITY;
    size_t size = 0; // Size of our string vector

    res = malloc(capacity * sizeof(char*));

    if (res == NULL) {
        perror("malloc error");
        exit(EXIT_FAILURE);
    }

    while (1) {
        ssize_t nread = read(dir_fd, &dir_buffer, sizeof(dir_buffer));

        if (nread == -1) {
            perror("read error");
            exit(EXIT_FAILURE);
        }

        if (nread == 0) {
            break; // Reached end of directory
        }

        // Ensure enough memory has been allowed, realloc() if not
        if (size >= capacity) {
            capacity *= 2;
            res = realloc(res, capacity * sizeof(char*));
            if (res == NULL) {
                perror("realloc error");
                exit(EXIT_FAILURE);
            }
        }

        // Now allocate memory for the current filename string
        res[size] = malloc(MAX_FILENAME_LENGTH);

        if (res[size] == NULL) {
            perror("malloc error");
            exit(EXIT_FAILURE);
        }

        // Copy directory name to array
        strncpy(res[size], dir_buffer.dir_name, MAX_FILENAME_LENGTH);

    }

    close(dir_fd);
}
