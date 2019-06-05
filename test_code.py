from numseq.fib import fib
from numseq.geo import *
from numseq.prime import *
import timeit

start = timeit.timeit()

print ("\nFibonacci")
for i in range(10):
    print ("{}: {}".format(i, fib(i)))


print("\nGeometric numbers (square, triangle, cube)")
for i in range(10):
    print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))


print ("\nPrimes")
prime_list = primes(1000)
for p in prime_list[-10:]:
    print (p)
print ("Is 999981 prime? {}".format(is_prime(999981)))
print ("Is 999983 prime? {}".format(is_prime(999983)))

t = timeit.Timer(
    stmt='main()', 
    setup='import cProfile; import pstats'
)

total_time = timeit.timeit() - start
print(f'\n\nTotal time for test code: {total_time} sec')