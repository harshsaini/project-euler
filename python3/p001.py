"""
    Problem 1
    
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
"""

MAX_NUMBER: int = 999

# # Naive solution
# sum: int = 0
# for i in range(1, MAX_NUMBER):
#     sum += i if i % 3 == 0 or i % 5 == 0 else 0

# print(sum)

# Optimal Solution
def sum_counting_numbers(n: int) -> int:
    # sum of all numbers from 1 to `max_dividend` -> (n * (n+1))/2
    return (n * (n+1)) / 2

def sum_numbers_divisible_by_n(n: int, limit: int) -> int:
    # Perform a calculation similar to (1+2+...+(limit/n)) * n
    max_dividend: int = int(limit / n)
    sum_dividends: int = sum_counting_numbers(max_dividend)
    return sum_dividends * n

sum_multiples_3 = sum_numbers_divisible_by_n(3, MAX_NUMBER)
sum_multiples_5 = sum_numbers_divisible_by_n(5, MAX_NUMBER)
sum_multiples_15 = sum_numbers_divisible_by_n(15, MAX_NUMBER)

print(sum_multiples_3 + sum_multiples_5 - sum_multiples_15)
