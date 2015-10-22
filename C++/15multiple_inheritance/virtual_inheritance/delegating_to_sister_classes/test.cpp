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

class transmitter : public virtual base {
    public:
        virtual void write() {
            cout << "in transmitter's write" << endl;
            read();
        }
};

class receiver : public virtual base {
    public:
        virtual void read() {
            cout << "in receiver's read" << endl;
        }
};

class virtual_radio : public transmitter {
};

class radio : public receiver, public transmitter {
    public:
        //virtual void write() {
        //    cout << "in radio's write" << endl;
        //}
};

void print_spr() {
    cout << "-------------" << endl;
}

int main() {
    radio *r = new radio();
    transmitter *r1 = r;
    receiver *r2 = r;

    r->write();

    print_spr();
    r1->write();

    print_spr();
    // no write() in receiver, TRANSMITTER's write get called
    r2->write();

    print_spr();
    r->base::write();

    // error: virtual_radio has no read() so is virtual
    //virtual_radio *vr = new virtual_radio();
}
