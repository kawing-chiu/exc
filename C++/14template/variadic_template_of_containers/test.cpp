#include <iostream>
#include <map>
#include <vector>
#include <utility>


template<typename T, typename U>
std::ostream& operator<<(std::ostream& o, std::pair<T, U> p) {
    std::cout << p.first << ": " << p.second;
    return o;
}

template<template<typename, typename...> class ContainerType,
    typename ValueType, typename... OtherArgs>
void print_container(const ContainerType<ValueType, OtherArgs...>& c) {
    for (auto& v : c) {
        std::cout << v << ' ';
    }
    std::cout << std::endl;
}

int main() {
    std::vector<double> v{3.5, 2.4, 100.0};
    print_container(v);

    std::map<std::string, int> m{{"one", 500}, {"try", 1000}};
    // has to implement '<<' operator for std::pair
    print_container(m);
}
