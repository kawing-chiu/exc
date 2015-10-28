#include <iostream>

using namespace std;


class Base {
    public:
        Base() {
            cout << "Base::Base()" << endl;
        }
        Base(int a, int b) : _a(a), _b(b) {
            cout << "Base::Base(a, b)" << endl;
        }
    private:
        int _a;
        int _b;
};

class D : public Base {
    public:
        D() {
            cout << "D::D()" << endl;
        }
        // this will call the DEFAULT ctor of Base, i.e. Base::Base():
        //D(int a, int b) {
        //    cout << "D::D(a, b)" << endl;
        //}
        D(int a, int b) : Base(a, b) {
            cout << "D::D(a, b)" << endl;
        }
};

int main() {
    D d;
    D d2(1, 3);
}
