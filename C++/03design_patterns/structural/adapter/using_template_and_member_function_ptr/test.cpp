#include <iostream>


using namespace std;


class Interface {
    public:
    virtual ~Interface() {}
    virtual void execute() = 0;
};

template<typename T>
class Adapter : public Interface {
    public:
    Adapter(T* obj, void(T::* old_member_func)()) : _obj(obj), _member_func(old_member_func) {}
    virtual void execute() override {
        (_obj->*_member_func)();
    }
    private:
    T* _obj;
    void (T::* _member_func)();
};


class A {
    public:
    ~A() {
        cout << "destructor of A" << endl;
    }
    void f() {
        cout << "calling A::f" << endl;
    }
};

class B {
    public:
    ~B() {
        cout << "destructor of B" << endl;
    }
    void g() {
        cout << "calling B::f" << endl;
    }
};

Interface **init_objects() {
    Interface **objs;
    objs = new Interface *[2];

    objs[0] = new Adapter<A>(new A(), &A::f);
    objs[1] = new Adapter<B>(new B(), &B::g);
    return objs;
}

int main() {
    Interface **objects = init_objects();
    for (int i = 0; i < 2; i++) {
        objects[i]->execute();
    }

    for (int i = 0; i < 2; i++) {
        delete objects[i];
    }
}
