#include <stdio.h>

void f();

// Since <stdio.h> is #included, 'static' cannot be used
// to mask global definition of fprintf.
// See also '04const'
// Multiple definition error:
//static void fprintf() {
//}

// this one will work:
//static double a = 50.0;

// this one will NOT work(multiple definition error):
//double a = 50.0;

int main() {
    extern double a;

    f();
    printf("%.2f\n", a);
}
