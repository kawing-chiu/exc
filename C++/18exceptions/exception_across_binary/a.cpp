#include "a.h"

const char * MyException::what() const throw() {
    return "Some Exception";
}
