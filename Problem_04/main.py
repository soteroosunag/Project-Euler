# Problem 4
#  A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Help funcition
def is_palindrome(n):
    string_version = str(n)
    mid = len(string_version)//2
    if len(string_version) % 2 == 0:
        if string_version[0:mid] == string_version[mid:][::-1]:
            return True
        else:
            return False
    else:
        if string_version[0:mid] == string_version[mid+1:][::-1]:
            return True
        else:
            return False
    
# Solution (naive)
def solution():
    curr = 0
    nums = []
    for i in range(999,100 ,-1):
        for j in range(990, 110, -11):
            if is_palindrome(i*j):
                if i*j > curr:
                    nums = [i, j]
                    curr = i*j
    print(nums)
    return curr

print(solution())