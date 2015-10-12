#include <iostream>
#include <string>

using namespace std;

void f(std::string s) {
    cout << s << endl;
}

int main() {
    string str1 = "hehe";
    cout << str1 << endl;

    f(str1);
    f("good");

    if (str1 == "hehe") {
        cout << "true" << endl;
    }

    for (auto iter = str1.begin(); iter != str1.end(); iter++) {
        cout << *iter << endl;;
    }

    string str2 = "This is a long string.";
    cout << "str2: " << str2 << endl;
    auto n = str2.find("long");
    cout << n << ": " << str2.substr(n) << endl;

}
