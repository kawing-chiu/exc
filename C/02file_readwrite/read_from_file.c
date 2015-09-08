#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    fp = fopen("mm", "r");
    if (fp == NULL) {
        fprintf(stderr, "Error: cannot open file\n");
        exit(EXIT_FAILURE);
    }

    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, fp)) != -1) {
        printf("Read %zd characters: %s", read, line);
    }

}
