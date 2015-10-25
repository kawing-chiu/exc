#include <functional>
#include <iostream>

using namespace std;

void print_num(int i) {
    cout << i << endl;
}

struct Foo {
    Foo(int num) : num_(num) {}
    void print_add(int i) const {
        cout << num_ + i << endl;
    }
    void set_num(int i) {
        num_ = i;
    }
    int num_;
};

struct PrintNum {
    void operator()(int i) const {
        cout << i << endl;
    }
};

int main() {
    std::function<void(int)> f_print_num = print_num;
    f_print_num(100);

    std::function<void()> f_print_135 = std::bind(print_num, 135);
    f_print_135();

    // call to member function:
    // note that Foo::print_add has only one int parameter
    std::function<void(const Foo &, int)> f_Foo_print_add = &Foo::print_add;
    //const Foo foo(100000);
    Foo foo(100000);
    f_Foo_print_add(foo, 1);

    std::function<void(const Foo *, int)> f_Foo_print_add1 = &Foo::print_add;
    f_Foo_print_add1(&foo, 2);

    // binding to foo:
    // by value:
    using std::placeholders::_1;
    std::function<void(int)> f_Foo_print_add2 = std::bind(&Foo::print_add, foo, _1);
    f_Foo_print_add2(20);
    foo.set_num(200000);
    f_Foo_print_add2(20);

    // by pointer:
    std::function<void(int)> f_Foo_print_add3 = std::bind(&Foo::print_add, &foo, _1);
    f_Foo_print_add3(33);
    foo.set_num(300000);
    f_Foo_print_add3(33);

    // call functor:
    std::function<void(int)> f_PrintNum_obj = PrintNum();
    f_PrintNum_obj(20);
}



