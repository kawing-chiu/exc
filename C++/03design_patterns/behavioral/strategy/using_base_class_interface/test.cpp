#include <iostream>
#include <string>
#include <functional>

using namespace std;


class Context {
    private:
        class Strategy *_strategy = nullptr;
    public:
        ~Context();
        enum class StrategyType {
            Good, Bad
        };
        void execute();

        // dark magic...
        // unnecessary, just ignore it
        template<typename... Args,
            typename std::enable_if<1 == sizeof...(Args), int>::type = 0>
        void set_strategy(StrategyType type, Args&&... params);

        template<typename... Args,
            typename std::enable_if<2 == sizeof...(Args), int>::type = 0>
        void set_strategy(StrategyType type, Args&&... params);
};

class Strategy {
    public:
        virtual ~Strategy() {}
        virtual void do_something() = 0;
};

class GoodStrategy : public Strategy {
    private:
        int _param;
    public:
        GoodStrategy(int param) : _param(param) {}
        void do_something() override {
            cout << "In GoodStrategy: my paramater is " << _param << endl;
        }
};

class BadStrategy : public Strategy {
    private:
        int _param1;
        double _param2;
    public:
        BadStrategy(int param1, int param2) : _param1(param1), _param2(param2) {}
        void do_something() override {
            cout << "In BadStrategy: my paramater is " << _param1 << " and " << _param2  << endl;
        }
};

//template<typename... Args>
//template<size_t N, typename... Args,
//    typename std::enable_if<N == sizeof...(Args), int>::type>
//void Context::set_strategy(StrategyType type, Args&&... params) {
//}

//template<typename... Args,
//    typename std::enable_if<1 == sizeof...(Args), int>::type>
template<typename... Args,
    typename std::enable_if<1 == sizeof...(Args), int>::type>
void Context::set_strategy(StrategyType type, Args&&... params) {
    delete _strategy;
    if (type == StrategyType::Good) {
        _strategy = new GoodStrategy(std::forward<Args>(params)...);
    }
}

template<typename... Args,
    typename std::enable_if<2 == sizeof...(Args), int>::type>
void Context::set_strategy(StrategyType type, Args&&... params) {
    delete _strategy;
    if(type == StrategyType::Bad) {
        _strategy = new BadStrategy(std::forward<Args>(params)...);
    }
}

void Context::execute() {
    _strategy->do_something();
}

Context::~Context() {
    delete _strategy;
}

int main() {
    Context *test = new Context;
    test->set_strategy(Context::StrategyType::Good, 50);
    test->execute();

    test->set_strategy(Context::StrategyType::Bad, 100, 200);
    test->execute();

}




