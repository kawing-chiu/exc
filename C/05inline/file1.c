#include <stdio.h>

// if compiled using '-O', this inline
// version will be used.
inline void f() {
    puts("inline f");
}

int main() {
    f();
}
