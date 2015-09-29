#include <iostream>


struct TestStruct
{
    char Type1[20];
    char Type2[10];
};


int main() {
    using namespace std;

    // not supported by gcc:
    TestStruct ts{ .Type2 = "hehe", .Type1 = "good" };

    cout << ts.Type1 << endl;
    cout << ts.Type2 << endl;

}
