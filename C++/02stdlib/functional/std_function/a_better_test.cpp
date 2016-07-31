#include <functional>
#include <iostream>

using namespace std;

class test {
private:
    int _x = 10;
    // variable for function pointer
    std::function< void ( int )> func;
    // default output function
    void my_default(int x) {
        cout << "x = " << x << endl ;
        cout << "_x = " << _x << endl;
    }
    std::function< void ( int )> _func = [&](int x) {
        cout << "int _x: " << _x << " x: " << x << endl;
    };

public:
    test(int x) {
        _func(100);
        _x = x;
    }
    void dummy(void) {
        // 1. Test - default output function
        cout << "my_default\n";
        func = std::bind(&test::my_default, this, std::placeholders::_1);
        // or 
        cout << "\n_func():\n";
        _func(20);

        cout << "\nfunc():\n";
        func = [&]( int i ){
            cout << "_x +1: " << _x + 1 << endl;
        };
        func(5);

        // 2. Test - special output function 2
        cout << "\nmy_func2\n";
        func =  [](int x)->int{ cout << "x =" << "  " << x << endl << endl; return 3; };
        func(5);
    }
};


// entry
int main() {
    cout << "Test Programm\n\n";

    test a(30);
    a.dummy();

    return 0;
}
