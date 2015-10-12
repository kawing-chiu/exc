#include <string>
#include <iostream>

using namespace std;

class Test {
    public:
    Test() {}
    Test(const char *s) {
        cout << "const char * ctor called" << endl;
        my_str = std::string(s);
    }
    Test(const Test& t) {
        cout << "in copy ctor" << endl;
        my_str = t.my_str;
    }
    std::string print() {
        return my_str;
    }
    private:
    std::string my_str;
};

int main() {
    // copy ctor is NOT called, copy initialization becomes direct 
    // initialization:
    Test s = "kkk";
    cout << s.print() << endl;

    // copy ctor is called:
    Test sb = s;
    cout << sb.print() << endl;
}
