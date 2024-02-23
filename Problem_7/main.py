# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def n_prime(n):
    if n == 1:
        return 2
    else:
        curr = 2
        prime = 3
        i = 3
        while curr <= n:
            if is_prime(i):
                curr += 1
                prime = i
            i += 2
        return prime

print(n_prime(10001))

