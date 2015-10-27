#include <iostream>
#include <string>
#include <functional>

using namespace std;


template<class S>
class Context {
    private:
        S *_strategy = nullptr;
    public:
        ~Context();
        Context(S *s) : _strategy(s) {}
        void execute();
};

template<class S>
void Context<S>::execute() {
    _strategy->do_something();
}

template<class S>
Context<S>::~Context() {
    delete _strategy;
}

// using template, no need for inheritance-based interface
//class Strategy {
//    public:
//        virtual ~Strategy() {}
//        virtual void do_something() = 0;
//};

class GoodStrategy {
    private:
        int _param;
    public:
        GoodStrategy(int param) : _param(param) {}
        void do_something() {
            cout << "In GoodStrategy: my paramater is " << _param << endl;
        }
};

class BadStrategy{
    private:
        int _param1;
        double _param2;
    public:
        BadStrategy(int param1, int param2) : _param1(param1), _param2(param2) {}
        void do_something() {
            cout << "In BadStrategy: my paramater is " << _param1 << " and " << _param2  << endl;
        }
};
int main() {
    Context<GoodStrategy> *test = new Context<GoodStrategy>(new GoodStrategy(50));
    test->execute();

    Context<BadStrategy> *test2 = new Context<BadStrategy>(new BadStrategy(100, 200));
    test2->execute();
}




