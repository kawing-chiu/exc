#include <mutex>
#include <thread>
#include <condition_variable>
#include <iostream>

using namespace std;


std::mutex g_lock;
std::condition_variable g_cond;

bool g_indicator = false;

void f(int i) {
    //no need for while if using lambda
    //while (true) {
        std::unique_lock<std::mutex> lock(g_lock);
        cout << "start waiting" << endl;
        g_cond.wait(lock, [] () { return g_indicator; });
        cout << "get signal" << endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        cout << "quit" << endl;
    //}
}

int main() {
    std::thread t(f, 0);
    std::this_thread::sleep_for(std::chrono::seconds(2));
    cout << "sending signal..." << endl;
    {
        std::unique_lock<std::mutex> lock(g_lock);
        g_indicator = true;
    }
    g_cond.notify_one();
    t.join();
}
