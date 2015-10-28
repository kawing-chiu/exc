#include <iostream>

using namespace std;

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
        virtual Shape* create() const = 0;   // Uses the default constructor
};

class Circle : public Shape {
    public:
        Circle* clone() const override;   // Covariant Return Types
        Circle* create() const override;   // Covariant Return Types
        void draw() override {
            cout << "Circle::draw" << endl;
        }
        void move() override {
            cout << "Circle::move" << endl;
        }
};

Circle* Circle::clone() const {
    cout << "Circle::clone" << endl;
    return new Circle(*this);
}
Circle* Circle::create() const {
    cout << "Circle::create" << endl;
    return new Circle();
}

int main() {
    Circle c;
    Shape *c2 = new Circle;

    Shape *s = c.clone();
    Shape *s2 = c2->clone();

    s->draw();
    s2->draw();
    delete s;
}



