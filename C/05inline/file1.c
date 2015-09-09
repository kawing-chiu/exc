#include <stdio.h>

// if compiled using '-O', this inline
// version will be used.
// without the 'extern' keyword, NO external callable
// version of this function will be produced.
inline void f() {
    puts("inline f");
}

int main() {
    f();
}
