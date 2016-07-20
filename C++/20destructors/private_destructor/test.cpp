// a class with PRIVATE dtor
struct A { private: ~A(); };
struct B : A {};

// not working 1:
//struct C : A { ~C() {}; };

int main() {
    // not working 2:
    //A a;
    // not working 3:
    //B b;
}
