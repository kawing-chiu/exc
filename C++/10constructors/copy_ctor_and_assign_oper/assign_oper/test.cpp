#include <iostream>

using namespace std;


class Test {
    public:
        // default copy ctor and assignment oper will be defined regardless of
        // whether a user-defined ctor is present.
        //Test() {}
        void set_i(int new_i) {
            i = new_i;
        }
        int get_i() {
            return i;
        }
    private:
        int i;
};

class Test2 {
    public:
        Test2() = default;
        Test2& operator=(const Test2& there);
        void set_i(int new_i) {
            i = new_i;
        }
        int get_i() {
            return i;
        }
    private:
        int i;
};

Test2& Test2::operator=(const Test2& there) {
    cout << "hello there" << endl;
    this->i = there.i;
    return *this;
}

int main() {
    Test t1, t2{};
    t1.set_i(10);

    cout << t2.get_i() << endl;
    t2 = t1;
    cout << t2.get_i() << endl;

    Test2 t3, t4{};
    t3.set_i(25);

    cout << t4.get_i() << endl;
    t4 = t3;
    cout << t4.get_i() << endl;

}
