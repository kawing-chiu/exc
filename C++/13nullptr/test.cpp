#include <iostream>

using namespace std;

template<typename F, typename A>
void fwd(F f, A a) {
    f(a);
}

void g(int *i) {
    cout << "in g" << endl;
}


int main() {
    g(NULL);
    g(0);

    fwd(g, nullptr);
    // not working:
    // fwd(g, NULL);
    // fwd(g, 0);
}
