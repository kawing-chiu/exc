#include <stdio.h>



// if declaration is needed, inline must also be used (but in C++
// it is not needed):
inline void f();


// if compiled using '-O', this inline
// version will be used.
// without the 'extern' keyword, NO external callable
// version of this function will be produced.
inline void f() {
    puts("inline f");
}


