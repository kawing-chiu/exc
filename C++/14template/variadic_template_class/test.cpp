#include <iostream>
#include <string>
#include <type_traits>



template<typename T, typename U>
struct is_same {
    static const bool value = false;
};

template<typename T>
struct is_same<T, T> {
    static const bool value = true;
};


template<class... Ts> struct Tup {};

// (recursive) specialization:
template<class T, class... Ts>
struct Tup<T, Ts...> : Tup<Ts...> {
    Tup(T t, Ts... ts) : Tup<Ts...>(ts...), tail(t) {}

    T tail;
};

template<size_t k, class T, class... Ts>
struct elem_type_holder {};

template<size_t k, class T, class... Ts>
struct elem_type_holder<k, Tup<T, Ts...>> {
    typedef typename elem_type_holder<k - 1, Tup<Ts...>>::type type;
};

template<class T, class... Ts>
struct elem_type_holder<0, Tup<T, Ts...>> {
    typedef T type;
};

template<size_t k, class... Ts>
typename std::enable_if<
    k == 0, typename elem_type_holder<0, Tup<Ts...>>::type&
>::type
get(Tup<Ts...> &t) {
    return t.tail;
}

template<size_t k, class T, class... Ts>
typename std::enable_if<
    k != 0, typename elem_type_holder<k, Tup<T, Ts...>>::type&
>::type
get(Tup<T, Ts...>& t) {
    Tup<Ts...>& base = t;
    return get<k - 1>(base);
}

int main() {
    Tup<double, int, std::string> t1(12.2, 50, "hehe");

    std::cout.setf(std::ios::boolalpha);
    // or:
    // std::cout << std::boolalpha;

    std::cout << is_same< elem_type_holder<0, Tup<double, int, std::string>>::type, double >::value << std::endl;
    std::cout << is_same< elem_type_holder<1, Tup<double, int, std::string>>::type, int >::value << std::endl;
    std::cout << is_same< elem_type_holder<2, Tup<double, int, std::string>>::type, std::string >::value << std::endl;

    std::cout << "0th elem: " << get<0>(t1) << std::endl;
    std::cout << "1th elem: " << get<1>(t1) << std::endl;
    std::cout << "2th elem: " << get<2>(t1) << std::endl;
}
