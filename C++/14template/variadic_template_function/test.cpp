#include <iostream>
#include <tuple>
#include <numeric>


using namespace std;

double sum() {
    return 0;
}

template<class Head, class ... Tail>
double sum(Head h, Tail ... t) {
    cout << __PRETTY_FUNCTION__ << endl;
    return h + sum(t ...);
}

template<typename T, typename... Params>
double sum2(Params... params) {
    std::array<T, sizeof...(params)> l = {params...};
    return std::accumulate(l.begin(), l.end(), 0.0);
}


template<class... Vars>
double foo(Vars... vars) {
    auto vars_tuple = std::make_tuple(vars...);
    cout << std::get<0>(vars_tuple) << endl;
    return std::get<1>(vars_tuple);
}

int main() {
    cout << sum(1, 3, 5, 7) << endl;
    // has to explicitly specify template argument:
    cout << "from sum2: " <<  sum2<int>(1, 3, 5, 7) << endl;

    cout << "foo return: " << foo(1, 3.0, 5) << endl;
    // error with tons of cryptic messages:
    //cout << "foo return: " << foo(1) << endl;
}
