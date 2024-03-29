def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def is_prime(n):
    if n <= 1:
        return False

    for x in range(2, n):
        if not n % x:
            return False
    return True