#include <iostream>


using namespace std;


class Test {
    private:
        int i = 0;
    public:
        void test1() {
            cout << "test1" << endl;
        }
        void test2() const {
            cout << "test2" << endl;
        }
};

int main() {
    const Test t{};

    // fails:
    //t.test1();

    // ok:
    t.test2();
}
