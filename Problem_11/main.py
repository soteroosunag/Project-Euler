# Problem 11
#
#
#
# The product of these numbers is 26 X 63 X 78 X 14 = 1788696
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 X 20 grid?

def largest_product_grid(grid, k):
    largest = -1
    curr = 1
    # Check horizontal
    left = 0
    right = 0
    for row in grid:
        while right < len(row):
            if right - left + 1 < k:
                curr *= right
            else:
                curr *= right
                curr /= left
                if curr > largest:
                    largest = curr
                left += 1
            right += 1
    # Check vertical
    # Check diagonals
    return largest