#include <iostream>

using namespace std;


class Test1 {
    public:
        // no Test() {}
        int get_i() {
            return i;
        }
    private:
        int i;
};

class Test2 {
    public:
        Test2() {}
        //Test2() : i() {}
        int get_i() {
            return i;
        }
    private:
        int i;
};

class Test3 {
    public:
        Test3() = default;
        int get_i() {
            return i;
        }
    private:
        int i;
};

int main() {
    Test1 t1, t2{};
    Test2 t3, t4{};

    cout << "t1: " << t1.get_i() << endl;
    cout << "t2: " << t2.get_i() << endl;
    cout << "t3: " << t3.get_i() << endl;
    cout << "t4: " << t4.get_i() << endl;

    Test3 t5, t6{};

    cout << "t5: " << t5.get_i() << endl;
    cout << "t6: " << t6.get_i() << endl;
}




