#include <iostream>

using namespace std;

namespace A {
    int i = 0;
}

namespace B {
    int i = 10;

    namespace C {
        // this using-directive will insert names into the GLOBAL namespace,
        // which is the enclosing namespace which contains A and the directive.
        using namespace A;

        void f() {
            // i is B::i, because A::i is inserted into global namespace.
            cout << i << endl;
        }
    }

}

int main() {
    B::C::f();
}
