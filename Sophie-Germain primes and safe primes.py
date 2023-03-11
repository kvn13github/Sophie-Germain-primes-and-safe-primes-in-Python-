import random
import math

# define Miller-Rabin primality test
def is_prime(n, k=10):
    # handle small values of n
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # write n-1 as 2^r * d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # run k iterations of Miller-Rabin test
    for _ in range(k):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False

    return True

# generate Sophie Germain primes and safe primes up to 10 digits
print("Generating Sophie Germain primes up to 10 digits:")
sophie_primes = []
for n in range(10**9, 10**10):
    if is_prime(n) and is_prime(2*n+1):
        sophie_primes.append(n)
        print(n, end=", ")

print("\n\nGenerating safe primes up to 10 digits:")
safe_primes = []
for n in sophie_primes:
    if is_prime((n-1)//2):
        safe_primes.append(n)
        print(n, end=", ")

# print results
print("\n\nSophie Germain primes:")
print(sophie_primes)
print("\nSafe primes:")
print(safe_primes)
