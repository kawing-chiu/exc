#include <iostream>


using namespace std;

template<typename... Args>
void test(Args... args) {
    cout << "calling..." << endl;
}


int main() {
    void (*f1)(void);
    f1 = test;

    void (*f2)(int nReason);
    f2 = test;

    f1();
    f2(5);
}
