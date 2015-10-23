#include <iostream>
#include <vector>

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
        virtual void execute(int &) = 0;
};

class SimpleCommand : public Command {
    private:
        typedef void (Number:: *Action)(int &);
        Number *_receiver;
        Action _action;
    public:
        SimpleCommand(Number *rec, Action act) :
            _receiver(rec), _action(act) {}
        void execute(int &num) override {
            (_receiver->*_action)(num);
        }
};

class MacroCommand : public Command {
    private:
        std::vector<Command *> cmd_list;
    public:
        void add(Command *cmd) {
            cmd_list.push_back(cmd);
        }
        void execute(int &num) override {
            for (size_t i = 0; i < cmd_list.size(); i++) {
                cmd_list[i]->execute(num);
            }
        }
};

int main() {
    Number num;

    //Command *cmd = new SimpleCommand(&num, &Number::dubble);
    //int i = 30;
    //cmd->execute(i);

    Command *commands[3];
    commands[0] = new SimpleCommand(&num, &Number::dubble);

    MacroCommand two;
    two.add(commands[0]);
    two.add(commands[0]);
    commands[1] = &two;

    MacroCommand four;
    four.add(commands[1]);
    four.add(commands[1]);
    commands[2] = &four;

    int i = 10;
    commands[2]->execute(i);
}



