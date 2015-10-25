#include <iostream>
#include <vector>
#include <functional>

using namespace std;


class Number {
    public:
        void dubble(int &value) {
            cout << "dubbling: " << value;
            value *= 2;
            cout << " result: " << value << endl;
        }
        void tripel(int &value, double test) {
            cout << "tripelling: " << value;
            value *= 3;
            cout << " result: " << value << endl;
        }
};

class Command {
    public:
        // a virtual destructor is necessary:
        virtual ~Command() {};
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
        int operator()() {
            execute();
            return 300;
        }
        // not working, virtual function cannot be template:
        //template<typename... Args>
        //void execute(Args&&... params) {
        //    _action(std::forward<Args>(params)...);
        //}
        void execute() {
            _action();
        }
};

int main() {
    Number num;

    Command *cmd = new SimpleCommand(&num, &Number::dubble, 50);
    cmd->execute();

    int j = (*dynamic_cast<SimpleCommand *>(cmd))();
    cout << "returned: " << j << endl;

    cmd->execute();
    delete cmd;

    int i = 30;
    Command *cmd2 = new SimpleCommand(&num, &Number::tripel, i, 20.0);
    cmd2->execute();
}
