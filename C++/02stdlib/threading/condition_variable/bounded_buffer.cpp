#include <iostream>
#include <mutex>
#include <thread>
#include <condition_variable>

using namespace std;

std::mutex g_stdout_lock;

struct BoundedBuffer {
    int* buffer;
    int capacity;

    int front;
    int rear;
    int count;

    std::mutex lock;

    std::condition_variable not_full;
    std::condition_variable not_empty;

    BoundedBuffer(int capacity) : capacity(capacity), front(0), rear(0), count(0) {
        buffer = new int[capacity];
    }

    ~BoundedBuffer(){
        delete[] buffer;
    }

    void deposit(int data){
        std::unique_lock<std::mutex> l(lock);

        g_stdout_lock.lock();
        cout << ">> waiting for not_full" << endl;
        g_stdout_lock.unlock();

        not_full.wait(l, [this](){ return count != capacity; });

        g_stdout_lock.lock();
        cout << ">> not_full signal get" << endl;
        g_stdout_lock.unlock();

        buffer[rear] = data;
        rear = (rear + 1) % capacity;
        ++count;

        g_stdout_lock.lock();
        cout << "**sending signal to not_empty" << endl;
        g_stdout_lock.unlock();
        not_empty.notify_one();
    }

    int fetch(){
        std::unique_lock<std::mutex> l(lock);

        g_stdout_lock.lock();
        cout << ">> waiting for not_empty" << endl;
        g_stdout_lock.unlock();

        not_empty.wait(l, [this](){ return count != 0; });

        g_stdout_lock.lock();
        cout << ">> not_empty signal get" << endl;
        g_stdout_lock.unlock();

        int result = buffer[front];
        front = (front + 1) % capacity;
        --count;

        cout << "**sending signal to not_full" << endl;
        not_full.notify_one();

        return result;
    }
};

void consumer(int id, BoundedBuffer& buffer){
    for(int i = 0; i < 20; ++i){
        g_stdout_lock.lock();
        std::cout << "Consumer " << id << " about to fetch" << std::endl;
        g_stdout_lock.unlock();

        int value = buffer.fetch();

        g_stdout_lock.lock();
        std::cout << "Consumer " << id << " fetched " << value << std::endl;
        g_stdout_lock.unlock();
        std::this_thread::sleep_for(std::chrono::milliseconds(250));
    }
}

void producer(int id, BoundedBuffer& buffer){
    for(int i = 0; i < 30; ++i){
        g_stdout_lock.lock();
        std::cout << "Producer " << id << " about to deposit" << std::endl;
        g_stdout_lock.unlock();

        buffer.deposit(i);

        g_stdout_lock.lock();
        std::cout << "Producer " << id << " deposited " << i << std::endl;
        g_stdout_lock.unlock();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }
}

int main(){
    BoundedBuffer buffer(20);

    std::thread c1(consumer, 0, std::ref(buffer));
    std::thread c2(consumer, 1, std::ref(buffer));
    std::thread c3(consumer, 2, std::ref(buffer));
    std::thread p1(producer, 0, std::ref(buffer));
    std::thread p2(producer, 1, std::ref(buffer));

    c1.join();
    c2.join();
    c3.join();
    p1.join();
    p2.join();

    return 0;
}
