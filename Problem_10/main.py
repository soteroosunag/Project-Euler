# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below two million

def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def summation_of_primes(n):
    if n < 2:
        return 0
    elif n == 3:
        return 2
    else:
        sum = 2
        curr = 3
        while curr < n:
            if is_prime(curr):
                sum += curr
            curr += 2
        return sum
    
print(summation_of_primes(2000000))