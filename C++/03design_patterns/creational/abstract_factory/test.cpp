#include <iostream>

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
        virtual Widget *create_button() = 0;
        virtual Widget *create_menu() = 0;
};

class LinuxFactory : public Factory {
    public:
        Widget *create_button() override {
            return new LinuxButton;
        }
        Widget *create_menu() override {
            return new LinuxMenu;
        }
};

class WindowsFactory : public Factory {
    public:
        Widget* create_button() {
            return new WindowsButton;
        }
        Widget* create_menu()   {
            return new WindowsMenu;
        }
};

void display_window(Factory *factory) {
    Widget *w[] = { factory->create_button(), factory->create_menu() };
    for (size_t i = 0; i < size_of_array(w); i++) {
        w[i]->draw();
    }
}

int main() {
#ifdef WINDOWS
    Factory *factory = new WindowsFactory;
#else
    Factory *factory = new LinuxFactory;
#endif

    display_window(factory);
}


