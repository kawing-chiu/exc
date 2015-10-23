#include <iostream>
#include <vector>
#include <functional>

using namespace std;


class Number {
    public:
        void dubble(int &value) {
            value *= 2;
            cout << value << endl;
        }
};

class Command {
    public:
        virtual void execute() = 0;
};

class SimpleCommand : public Command {
    private:
        //using Action = std::function<void(Number *, int &)>;
        using DeferredAction = std::function<void()>;
        DeferredAction _action;
    public:
        template<typename Action, typename... Args>
        SimpleCommand(Number *rec, Action act, Args&&... params) {
            _action = std::bind(act, rec, std::forward<Args>(params)...);
        }
        void execute() {
            _action();
        }
};

int main() {
    Number num;

    int i = 30;
    Command *cmd = new SimpleCommand(&num, &Number::dubble, 50);
    cmd->execute();
}
