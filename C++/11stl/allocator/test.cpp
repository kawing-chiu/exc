#include <memory>
#include <iostream>
#include <string.h>

int main() {
    std::allocator<int> allo_int;
    int *a = allo_int.allocate(20);

    a[19] = 5;
    std::cout << a[0] << a[19] << std::endl;

    allo_int.deallocate(a, 20);
    std::cout << a[0] << a[19] << std::endl;


    std::allocator<std::string> allo_str;
    decltype(allo_int)::rebind<std::string>::other allo_str2;

    std::string *s = allo_str2.allocate(2);
    allo_str2.construct(s, "foo");
    allo_str2.construct(s + 1, "hehehe");

    std::cout << s[0] << " " << s[1] << std::endl;

    allo_str2.destroy(s);
    std::cout << s[0] << " " << s[1] << std::endl;

    allo_str2.deallocate(s, 2);
    // this will core dump
    //std::cout << s[0] << " " << s[1] << std::endl;

}
