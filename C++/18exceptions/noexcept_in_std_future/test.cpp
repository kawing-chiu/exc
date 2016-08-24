#include <future>
#include <iostream>

void good_func() noexcept
{
    throw std::exception();
}


int main() {
    auto test = std::async(std::launch::async, good_func);
    try {
        test.get();
    } catch (const std::exception &e) {
        std::cout << "nothing" << std::endl;
    }
}
