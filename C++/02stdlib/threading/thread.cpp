#include <thread>
#include <iostream>

using namespace std;

void f() {
    cout << "Before" << endl;
    std::this_thread::sleep_for(chrono::seconds(2));
    cout << "After" << endl;
}

int main() {
    std::thread t(f);
    cout << "In main thread" << endl;
    std::this_thread::sleep_for(chrono::milliseconds(500));
    cout << "main thread waiting" << endl;
    t.join();
}
