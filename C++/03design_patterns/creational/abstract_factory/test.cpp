#include <iostream>
#include <memory>

using namespace std;

template<typename T, size_t N>
constexpr size_t size_of_array(T (&)[N]) {
    return N;
}


class Widget {
    public:
        virtual void draw() = 0;
};

class LinuxButton : public Widget {
    public:
        void draw() { cout << "LinuxButton\n"; }
};
class LinuxMenu : public Widget {
    public:
        void draw() { cout << "LinuxMenu\n"; }
};
class WindowsButton : public Widget {
    public:
        void draw() { cout << "WindowsButton\n"; }
};
class WindowsMenu : public Widget {
    public:
        void draw() { cout << "WindowsMenu\n"; }
};


class Factory {
    public:
        //virtual Widget *create_button() = 0;
        virtual std::unique_ptr<Widget> create_button() = 0;
        //virtual Widget *create_menu() = 0;
        virtual std::unique_ptr<Widget> create_menu() = 0;
};

class LinuxFactory : public Factory {
    public:
        std::unique_ptr<Widget> create_button() override {
            // memory lost!
            //return new LinuxButton;
            return std::unique_ptr<Widget>(new LinuxButton);
        }
        std::unique_ptr<Widget> create_menu() override {
            // memory lost!
            //return new LinuxMenu;
            return std::unique_ptr<Widget>(new LinuxMenu);
        }
};

class WindowsFactory : public Factory {
    public:
        std::unique_ptr<Widget> create_button() {
            //return new WindowsButton;
            return std::unique_ptr<Widget>(new WindowsButton);
        }
        std::unique_ptr<Widget> create_menu()   {
            //return new WindowsMenu;
            return std::unique_ptr<Widget>(new WindowsMenu);
        }
};

void display_window(Factory *factory) {
    //Widget *w[] = { factory->create_button(), factory->create_menu() };
    std::unique_ptr<Widget> w[] = { factory->create_button(), factory->create_menu() };
    for (size_t i = 0; i < size_of_array(w); i++) {
        w[i]->draw();
    }
}

int main() {
#ifdef WINDOWS
    // memory lost!
    //Factory *factory = new WindowsFactory;
    std::unique_ptr<Factory> factory(new WindowsFactory);
#else
    // memory lost!
    //Factory *factory = new LinuxFactory;
    // wrong way:
    //std::unique_ptr<Factory> factory = new LinuxFactory;
    std::unique_ptr<Factory> factory(new LinuxFactory);
#endif

    // for normal pointer:
    //display_window(factory);
    display_window(factory.get());
}


