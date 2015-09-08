#include <stdio.h>
#include <time.h>

#define SEC_TO_NS 1e9


static double ts_to_double(struct timespec *ts) {
    double res = 0.0;
    res = ts->tv_sec + ts->tv_nsec / SEC_TO_NS;
    return res;
}

static double test() {
    struct timespec s;
    struct timespec e;

    clock_gettime(CLOCK_REALTIME, &s);
    double stime = ts_to_double(&s);

    clock_gettime(CLOCK_REALTIME, &e);
    double etime = ts_to_double(&e);


    double diff = etime - stime;
    return diff;
}

int main() {
    int n = 100000;
    double sum = 0.0;

    for (int i = 0; i < n; i++) {
        sum += test();
    }

    double res_in_s = sum / n;
    fprintf(stdout, "Time in ns: %f\n", res_in_s * SEC_TO_NS);
}

