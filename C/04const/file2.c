

//static int const ddd = 123;

// In C, unlike in C++, const variables still have external linkage.
int const ddd = 123;

double kkk = 5.0;

// Will result in 'multiple definition'
//int f() {
static int f() {
    return 3;
}

void g() {
    f();
}
