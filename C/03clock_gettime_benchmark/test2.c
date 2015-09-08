#include <time.h>
#include <stdio.h>
#include <stdint.h>

uint64_t nanotime(const struct timespec *ts)
{
   return (ts->tv_sec * 1e9) + ts->tv_nsec;
}


int main() {
    uint64_t    n=50000;
    uint64_t    sum=0;
    uint64_t    latency=0;

    for (uint64_t i = 0; i < n; i++) {
        struct timespec start;
        struct timespec end;
        clock_gettime(CLOCK_REALTIME, &start);
        clock_gettime(CLOCK_REALTIME, &end);
        sum += nanotime(&end) - nanotime(&start);
    }
    
    printf("Latency: %f ns\n", (double)sum / n);
}
