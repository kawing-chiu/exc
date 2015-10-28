#include <iostream>
#include <vector>

using namespace std;

// example from https://sourcemaking.com/design_patterns/factory_method/cpp/1

class Stooge
{
    public:
        // Factory Method
        virtual ~Stooge() {}
        static Stooge *make_stooge(int choice);
        virtual void slap_stick() = 0;
};

int main()
{
    vector<Stooge *> roles;
    int choice = -1;
    while (true)
    {
        cout << "Larry(1) Moe(2) Curly(3) Go(0): ";
        // choice will get 0 if input is not a number!
        cin >> choice;
        cout << "got choice: " << choice << endl;
        if (choice == 0) {
            cout << "breaking" << endl;
            break;
        }
        roles.push_back(Stooge::make_stooge(choice));
    }
    cout << "roles.size(): " << roles.size() << endl;
    for (size_t i = 0; i < roles.size(); i++)
        roles[i]->slap_stick();
    for (size_t i = 0; i < roles.size(); i++)
        delete roles[i];
}

class Larry: public Stooge
{
    public:
        void slap_stick()
        {
            cout << "Larry: poke eyes\n";
        }
};
class Moe: public Stooge
{
    public:
        void slap_stick()
        {
            cout << "Moe: slap head\n";
        }
};
class Curly: public Stooge
{
    public:
        void slap_stick()
        {
            cout << "Curly: suffer abuse\n";
        }
};

Stooge *Stooge::make_stooge(int choice)
{
    if (choice == 1)
        return new Larry;
    else if (choice == 2)
        return new Moe;
    else
        return new Curly;
}
