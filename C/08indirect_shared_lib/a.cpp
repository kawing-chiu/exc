#include <stdio.h>

// if extern is not used, --as-needed takes effect and neither libb.so nor 
// libd.so is linked
//int a;
extern int a;
int main() {
    printf("%d", a);
    return a;
}
