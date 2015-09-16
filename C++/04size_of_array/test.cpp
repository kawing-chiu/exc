#include <iostream>


template <typename T, size_t N>
constexpr size_t size_of_array(T (&)[N]) {
    return N;
}

using namespace std;

int main() {
    char array[20];
    //size_t size = sizeof(array) / sizeof(array[0]);
    size_t size = size_of_array(array);
    cout << "Hello" << endl;
    cout << "size: " << size << endl;
}

