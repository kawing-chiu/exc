#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    vector<int> v;
    v.push_back(3);
    v.push_back(10);
    v.push_back(33);

    for (size_t i = 0; i < v.size(); i++) {
        cout << "v[" << i << "]: " << v[i] << endl;
    }

    if (!v.empty()) {
        v.clear();
    }

    vector<int> vv;
    vv.push_back(10);
    v.push_back(10);

    if (v == vv) {
        cout << "the same!" << endl;
    }

    v.push_back(20);
    v.push_back(30);

    using iter_type = std::vector<int>::iterator;
    for (iter_type it = v.begin(); it != v.end(); it++) {
        cout << *it << endl;
    }

    for (auto& it : v) {
        it += 1;
    }

    // using for_each
    std::for_each(v.begin(), v.end(), [](int &elem) {
        elem += 2;
    });

    // WRONG!!!
    // without reference, cannot get reference:
    //for (auto it : v) {
    //    auto i  = &it - &v[0];
    //    cout << "v[" << i << "]: " << it << endl;
    //}

    // when using auto, getting the index is not that convenient:
    for (auto& it : v) {
        auto i  = &it - &v[0];
        cout << "v[" << i << "]: " << it << endl;
    }


}
