#include <iostream>
#include <memory>


using namespace std;


// new interface
class Interface {
    public:
        virtual ~Interface() {}
        virtual void execute() = 0;
};

template<typename T>
class Adapter : public Interface {
    public:
        ~Adapter() {
            cout << "dtor of Adapter" << endl;
            // note that _obj will NOT be freed automatically
            // a compiler-defined default dtor will NOT work either
            delete _obj;
        }
        Adapter(T* obj, void(T::* old_member_func)()) : _obj(obj), _member_func(old_member_func) {}
        virtual void execute() override {
            cout << "Adapter: calling old interface:" << endl;
            (_obj->*_member_func)();
        }
    private:
        T* _obj;
        void (T::* _member_func)();
};

// a new version using smart pointer
template<typename T>
class Adapter2 : public Interface {
    public:
        // no customized destructor
        Adapter2(T* obj, void(T::* old_member_func)()) : _obj(std::move(unique_ptr<T>(obj))), _member_func(old_member_func) {}
        virtual void execute() override {
            cout << "Adapter2: calling old interface:" << endl;
            (_obj.get()->*_member_func)();
        }
    private:
        unique_ptr<T> _obj;
        void (T::* _member_func)();
};


// old classes to be wrapped
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

    // this alone will NOT work (check it with valgrind):
    //delete [] objects;

    // destruction should be done like this:
    for (int i = 0; i < 2; i++) {
        delete objects[i];
    }
    delete [] objects;

    cout << "-------------" << endl;

    // test the smart pointer version
    Adapter2<A> a(new A(), &A::f);
    a.execute();

}




