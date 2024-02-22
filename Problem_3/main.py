# Problem 3
# The Prime factors of 13195 are 5, 7, 13, and 29
# What is the largest prime factor of the number 600851475143

"""
INEFFICIENT SOLUTION: SIEVE OF ERATOSTHENES
def sieve_of_eratosthenes_solution(n):
    nums = [True for _ in range(n+1)]
    p = 2
    largest_factor = 0
    while (p*p < n):
        if nums[p] == True:
            if p % n == 0:
                largest_factor = p
            for i in range(p*p, n+1, p):
                nums[i] = False
        p += 1
    
    if largest_factor == 0:
        return n
    else:
        return largest_factor

test = 600851475143
print(sieve_of_eratosthenes_solution(test))
"""

# EFFICIENT SOLUTION: FACTORIZATION

def find_largest_prime_factor(n):
    largest = 0
    while n % 2 == 0:
        n //= 2
    currPrime = 3
    while currPrime*currPrime <= n:
        while n % currPrime == 0:
            n //= currPrime
        currPrime += 2

    if largest == 0:
        return n
    else:
        return largest
    
print(find_largest_prime_factor(600851475143))
    
        
        
