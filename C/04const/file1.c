#include <stdio.h>

// Global definition can be masked by 'static',
// as long as other files are not #included.
// Note that this does not conflict with file3's 'extern' !
// See also '01include_files'.
static int kkk = 10;

// Not working:
//int kkk = 10;

int main() {
    extern int ddd;
    printf("%d\n", ddd);
    printf("%d\n", kkk);

    void f();
    f();
}
