#include <iostream>

void f()
{
    throw 15;
}

int main() {
    try {
        f();
    } catch (...) {
        std::cout << "here" << std::endl;
    }
}
