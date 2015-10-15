#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    std::map<string, int> test_map;
    test_map["hehe"] = 50;
    test_map["quant"] = 100;

    cout << "size: " << test_map.size() << endl;

    // initialized to 0 when accessed:
    cout << test_map["kkk"] << endl;
    cout << "size: " << test_map.size() << endl;
}
