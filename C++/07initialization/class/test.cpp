#include <iostream>

using namespace std;

class Test {
    public:
        Test(int i, int j1, int j2) : i_(i), j_{j1, j2} {}
        void test() {
            cout << "i: " << i_ << endl;
            cout << "j: " << j_[0] << "," << j_[1] << endl;
        }
    private:
        int i_;
        int j_[2];
};

int main() {
    Test t1(10, 11, 12);
    t1.test();

    Test t2{20, 21, 22};
    t2.test();

    Test(100, 101, 102).test();

    // not working:
    //Test t0;

}
