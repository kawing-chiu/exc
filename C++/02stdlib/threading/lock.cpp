#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>

using namespace std;

std::mutex g_lock;

void f(int i) {
    g_lock.lock();

    int sec = rand() % 5;
    std::cout << "enter " << i << std::endl;
    std::cout << "sleeping for " << sec << "s" << std::endl;

    std::this_thread::sleep_for(std::chrono::seconds(sec));

    g_lock.unlock();
}

int main() {
    std::thread t1(f, 1);
    std::thread t2(f, 2);
    std::thread t3(f, 3);

    t1.join();
    t2.join();
    t3.join();
}
