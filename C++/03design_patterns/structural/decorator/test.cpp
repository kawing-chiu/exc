#include <iostream>
#include <string>
#include <memory>

using namespace std;


class Interface {
    public:
        virtual ~Interface() {}
        virtual void write(string &) = 0;
        virtual void read(const string &) = 0;
};

class Core : public Interface {
    public:
        ~Core() {
            cout << "dtor of Core" << endl;
        }
        void write(string &s) override {
            s += " core ";
        }
        void read(const string &s) override {
            cout << "read: " << s << endl;;
        }
};

class Decorator : public Interface {
    private:
        unique_ptr<Interface> _inner;
        //Interface *_inner;
    public:
        Decorator(Interface *i) : _inner(i) {}
        ~Decorator() {
            cout << "dtor of Decorator, deleting _inner..." << endl;
            //delete _inner;
        }
        void write(string &s) override {
            _inner->write(s);
        }
        void read(const string &s) override {
            _inner->read(s);
        }
};

class Wrapper : public Decorator {
    private:
        string _forward, _backward;
    public:
        Wrapper(Interface *i, string s) : Decorator(i), _forward(s) {
            for (auto iter = s.rbegin(); iter != s.rend(); iter++) {
                _backward += *iter;
            }
        }
        ~Wrapper() {
            cout << "dtor of Wrapper (" << _forward << ")" << endl;
        }
        void write(string &s) override {
            s += _forward + " ";
            // All decorators call functions of the core object like this:
            Decorator::write(s);
            s += " " + _backward;
        }
};

int main() {
    Interface *object = new Wrapper(new Wrapper(new Core(), "123"), "abc");
    string buf;
    object->write(buf);
    object->read(buf);

    delete object;
}






