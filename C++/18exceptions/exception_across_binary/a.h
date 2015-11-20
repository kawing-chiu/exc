#ifndef _A_H
#define _A_H

// compile with hidden visibility
// MyException is throw in another shared lib b, and catched in c

#define EXPORT __attribute__ ((visibility ("default")))

#include <exception>


// does not work if EXPORT is not present:
//struct MyException : public std::exception {
// check with nm -CD liba.so to see the effect of EXPORT
struct EXPORT MyException : public std::exception {
    const char * what() const throw(); 
};


#endif // End of _A_H
