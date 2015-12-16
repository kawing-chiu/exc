#include <iostream>
#include <vector>

using namespace std;

class Subject {
    private:
        vector<class Observer *> _views;
        int _value;
    public:
        void attach(Observer *obs) {
            _views.push_back(obs);
        }
        void set_val(int val) {
            _value = val;
            notify();
        }
        int get_val() {
            return _value;
        }
        void notify();
};

// many observers subscribing changes to the subject
class Observer {
    private:
        Subject *_model;
        int _denom;
    public:
        Observer(Subject *model, int denom) : _model(model), _denom(denom) {
            model->attach(this);
        }
        virtual void update() = 0;
    protected:
        Subject *get_subject() {
            return _model;
        }
        int get_devisor() {
            return _denom;
        }
};

void Subject::notify() {
    for (size_t i = 0; i < _views.size(); i++) {
        _views[i]->update();
    }
}


class DivObserver : public Observer {
    public:
        DivObserver(Subject *model, int denom) : Observer(model, denom) {}
        void update() {
            int val = get_subject()->get_val(),
                d = get_devisor();
            cout << "In DivObserver: val: " << val << " div: " << d << endl;
        }
};

class ModObserver : public Observer {
    public:
        ModObserver(Subject *model, int denom) : Observer(model, denom) {}
        void update() {
            int val = get_subject()->get_val(),
                d = get_devisor();
            cout << "In ModObserver: val: " << val << " div: " << d << endl;
        }
};

int main() {
    Subject sub;
    DivObserver(&sub, 5);
    DivObserver(&sub, 3);
    ModObserver(&sub, 2);
    sub.set_val(8);
    sub.set_val(10);
}
