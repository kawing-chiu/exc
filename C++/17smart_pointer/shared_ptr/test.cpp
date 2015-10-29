#include <iostream>
#include <memory>

using std::cout;
using std::endl;
using std::shared_ptr;

class Test {
    public:
        Test(int a = 100) : _a(a) {}
        ~Test() {
            cout << "destructing Test: " << _a << endl;
        }
        int get_a() {
            return _a;
        }
        void set_a(int a) {
            _a = a;
        }
        void print_a() {
            cout << "a: " << _a << endl;
        }
    private:
        int _a;
};

void f() {
    shared_ptr<Test> p1(new Test[2], [](Test *p) {
        delete [] p;
    });
    // not working:
    // shared_ptr has no native support for array
    //p1[0].print_a();
    p1.get()[0].set_a(111);
    (p1.get() + 1)->set_a(115);

    cout << "use count: " << p1.use_count() << endl;
    shared_ptr<Test> p11(p1);
    cout << "use count: " << p1.use_count() << endl;

    // the old way:
    Test *p2 = new Test[2]();
    p2->set_a(200);
    p2[1].set_a(300);
    delete [] p2;
}

int main() {
    cout << "before f" << endl;
    f();
    cout << "after f" << endl;
}
