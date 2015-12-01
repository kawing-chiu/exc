#include <iostream>

using namespace std;

// this example is from 
// https://isocpp.org/wiki/faq/virtual-functions#virtual-ctors

class Shape {
    public:
        virtual ~Shape() { }                 // A virtual destructor

        virtual void draw() = 0;             // A pure virtual function
        virtual void move() = 0;

        virtual Shape* clone() const {   // Uses the copy constructor
            cout << "Shape::clone" << endl;
            Shape *s = nullptr;
            return s;
        }
        virtual Shape* create(int x) const = 0;   // Uses the default constructor
};

class Circle : public Shape {
    public:
        Circle(int x) : _x(x) {}
        Circle* clone() const override;   // Covariant Return Types
        Circle* create(int x) const override;   // Covariant Return Types
        void draw() override {
            cout << "Circle::draw x: " << _x << endl;
        }
        void move() override {
            cout << "Circle::move" << endl;
        }
    private:
        int _x = 0;
};

Circle* Circle::clone() const {
    cout << "Circle::clone" << endl;
    return new Circle(*this);
}
Circle* Circle::create(int x) const {
    cout << "Circle::create" << endl;
    return new Circle(x);
}

int main() {
    Circle c(10);
    Shape *c2 = new Circle(20);

    Shape *s = c.clone();
    Shape *s2 = c2->clone();

    s->draw();
    s2->draw();
    delete s;
}



