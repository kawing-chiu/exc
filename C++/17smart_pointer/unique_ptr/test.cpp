#include <iostream>
#include <memory>


using namespace std;

class Base {
    public:
        virtual ~Base() {
            cout << "destructing Base" << endl;
        }
        virtual void print_a() {
            cout << "I'm Base, I have no 'a' to print." << endl;
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

unique_ptr<Test> f() {
    std::unique_ptr<Test> p1(new Test);
    p1->set_a(250);
    cout << "p1: ";
    p1->print_a();

    std::unique_ptr<Base> p2(new Test);
    // not working:
    //p2->set_a(300);
    //dynamic_cast<Test *>(p2)->set_a(300);
    cout << "p2 (using base pointer): ";
    p2->print_a();

    // .get() method return the raw pointer:
    dynamic_cast<Test *>(p2.get())->set_a(300);
    p2->print_a();

    // can return directly from function, will be automatically moved
    return p1;
}

// this is the best to pass a unique_ptr to function (do not transfer 
// ownership)
// also works with non-smart pointer
void process_ptr1(Test &t) {
    t.set_a(t.get_a() + 10);
}

// this is also ok, by using const &, the function can use the pointer but 
// cannot claim its ownership
void process_ptr2(unique_ptr<Test> const &p) {
    p->set_a(p->get_a() + 20);
}

void transfer_ptr(unique_ptr<Test> p) {
    cout << "in transfer_ptr" << endl;
    p->set_a(500);
    p->print_a();
}

template<typename T>
class PtrBank {
    public:
        // note that std::move is mandatory
        PtrBank(unique_ptr<T> p) : _p(std::move(p)) {}
        void show_ptr() {
            _p->print_a();
        }
    private:
        unique_ptr<T> _p;
};

int main() {
    unique_ptr<Test> p1 = f();
    cout << "after f" << endl;
    p1->print_a();

    cout << "-------------" << endl;

    process_ptr1(*p1);
    p1->print_a();

    process_ptr2(p1);
    p1->print_a();

    // note that std::move is mandatory
    transfer_ptr(std::move(p1));
    cout << "returned from transfer_ptr()" << endl;
    // segmentation fault:
    //p1->print_a();

    cout << "-------------" << endl;

    // test transferring ownership to new class
    std::unique_ptr<Test> p2(new Test);
    p2->set_a(300);
    PtrBank<Test> bank(std::move(p2));
    bank.show_ptr();

    // not working:
    //PtrBank<Test> bank2(new Test);
    PtrBank<Test> bank2(unique_ptr<Test>(new Test));
    bank2.show_ptr();
}




