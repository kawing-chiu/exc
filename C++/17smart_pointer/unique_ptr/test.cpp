#include <iostream>
#include <memory>


using namespace std;

class Base {
    public:
        virtual ~Base() {}
        virtual void print_a() {
            cout << "I'm Base, I have no a to print." << endl;
        }
};

class Test : public Base {
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
        void print_a() override {
            cout << "Test's a: " << _a << endl;
        }
    private:
        int _a;
};

void f() {
    std::unique_ptr<Test> p1(new Test);
    p1->set_a(250);
    p1->print_a();

    std::unique_ptr<Base> p2(new Test);
    // not working:
    //p2->set_a(300);
    //dynamic_cast<Test *>(p2)->set_a(300);
    dynamic_cast<Test *>(p2.get())->set_a(300);
    p2->print_a();
}

int main() {
    cout << "before f" << endl;
    f();
    cout << "after f" << endl;
}




