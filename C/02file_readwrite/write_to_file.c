#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    fp = fopen("mm", "w");
    if (fp == NULL) {
        exit(EXIT_FAILURE);
    }

    puts("hello");
    fputs("hehe\n", fp);

    fclose(fp);
}
