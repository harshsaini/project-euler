"""
Problem 6 - Sum square difference
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

MAX_NUMBER = 100

# Naive Solution
a = list(range(1, MAX_NUMBER+1))
result = 0
for i in a:
    for j in a:
        if not i == j:
            result += i * j
print(result)
