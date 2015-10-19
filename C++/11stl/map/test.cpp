#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    std::map<string, int> test_map = {{"good", 10}};
    test_map["hehe"] = 50;
    test_map["quant"] = 100;

    cout << "size: " << test_map.size() << endl;

    // initialized to 0 when accessed using []:
    cout << test_map["kkk"] << endl;
    cout << "size: " << test_map.size() << endl;

    // looping
    typedef std::map<string, int>::iterator iter_type;
    for (iter_type it = test_map.begin(); it != test_map.end(); it++) {
        cout << it->first << ", " << it->second << endl;
    }

    for (auto it = test_map.begin(); it != test_map.end(); it++) {
        cout << it->first << ",, " << it->second << endl;
    }

    for (auto it : test_map) {
        cout << it.first << ",,, " << it.second << endl;
    }

    for (auto& it : test_map) {
        cout << it.first << ",,,, " << it.second << endl;
    }
}
