# see Readme file

# loop.pyx
def run_loop():
    cdef unsigned long long i
    cdef unsigned long long n = 1_000_000_000
    cdef unsigned long long x=0
    for i in range(n):
        x+= i
    print(x)
