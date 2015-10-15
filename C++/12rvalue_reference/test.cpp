#include <iostream>
#include <string>

using namespace std;


string get_str() {
    return "hehehe";
}

void f(string&& s) {
    cout << "in f: " << s << endl;
}

int main() {
    // not working:
    //string&& s = get_str();
    string&& s = get_str();
    s[2] = 'x';
    cout << s << endl;

    // no matching call:
    //f(s);
    f("ttt");
}
