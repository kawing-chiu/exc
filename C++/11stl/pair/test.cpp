#include <utility>
#include <tuple>
#include <string>
#include <iostream>

#include <typeinfo>

using namespace std;

int main() {
    std::pair<int, double> p;
    p = {10, 25.3};

    cout << p.first << " " << p.second << endl;
    cout << std::get<0>(p) << " " << std::get<1>(p) << endl;

    std::tuple<int, double, string> t;
    t = std::make_tuple(1, 10.0, "hehe");
    auto third = std::get<2>(t);
    cout << third << endl;
}
