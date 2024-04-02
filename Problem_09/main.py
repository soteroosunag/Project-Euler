# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000

def pythagorean_triplet(n):
    for i in range(1,n-2):
        for j in range(i+1, n-1):
            if i**2 + j**2 == (n-i-j)**2:
                return i*j*(n-i-j)
    return 0

print(pythagorean_triplet(1000))
