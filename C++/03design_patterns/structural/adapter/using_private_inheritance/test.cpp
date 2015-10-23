#include <iostream>


using namespace std;


class Interface {
    public:
    virtual ~Interface() {
        cout << "destructor of Interface" << endl;
    }
    virtual void execute() = 0;
};

class A {
    public:
    A(int x1, int x2) : _x1(x1), _x2(x2) {}
    //~A() {
    //    cout << "destructor of A" << endl;
    //}
    void f() {
        cout << "calling A::f" << endl;
    }
    void old_execute() {
        cout << "_x1: " << _x1 << " " << "_x2: " << _x2 << endl;
    }
    private:
    int _x1;
    int _x2;
};

class Adapter : public Interface, private A {
    public:
    Adapter(double y1, double y2, double z) : A(y1, y2), _z(z) {}
    virtual ~Adapter() {
        cout << "destructor of Adapter" << endl;
    }

    virtual void execute() override {
        old_execute();
    }

    using A::f;

    private:
    double _z;
};

int main() {
    //Adapter a(10, 20, 0.5);
    //a.f();

    //Adapter *b = new Adapter(20, 21, 3.5);
    //b->execute();
    //delete b;

    Interface *c = new Adapter(30, 32, 5.5);
    c->execute();
    dynamic_cast<Adapter *>(c)->f();
    delete c;

}
