#include <iostream>

using namespace std;


class base {
    public:
        virtual void read() = 0;
        virtual void write() {
            cout << "in base's write" << endl;
        };
        virtual ~base() {};
    private:
        int _i;
};

class transmitter : public base {
    public:
        virtual void write() override {
            cout << "in transmitter's write" << endl;
            read();
        }
        virtual void read() override {
            cout << "in transmitter's read" << endl;
        }
};      


class radio : public transmitter {
    public:
        virtual void read() override {
            cout << "in radio's read" << endl;
        }
        virtual void test() {
            cout << "in radio's test" << endl;
        }
};

void print_spr() {
    cout << "-------------" << endl;
}

int main() {
    radio *r = new radio();

    r->read();
    r->transmitter::read();

    //print_spr();

    //transmitter *t = new radio();
    //t->read();

    print_spr();

    base *b = new radio();
    // radio's read:
    b->read();
    // still radio's read:
    dynamic_cast<transmitter *>(b)->read();
    // finally, transmitter's read:
    dynamic_cast<transmitter *>(b)->transmitter::read();
    dynamic_cast<radio *>(b)->test();

    ///////////////////////
    print_spr();

    transmitter *t = new transmitter();
    t->read();
    transmitter *t2 = new radio();
    t2->read();
}











