#include <stdio.h>

void f();

// Since <stdio.h> is #included, 'static' cannot be used
// to mask global definition.
// See also '04const'
// Multiple definition error:
//static void fprintf() {
//}

int main() {
    extern double a;

    f();
    printf("%.2f\n", a);
}
