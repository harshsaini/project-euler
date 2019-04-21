"""
Problem 2 - Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

MAX_VALUE = 4 * 10**6

# # Naive solution
# def fib(limit: int) -> int:
#     sum = 0

#     y = 0
#     x = 1
#     while limit > x:
#         sum += x if x % 2 == 0 else 0
#         temp = x + y
#         y = x
#         x = temp
#     return sum

# print(fib(MAX_VALUE))

# Optimal Solution
def sum_even_fib(limit: int) -> int:
    def next_even_fib(a: int, b: int) -> int:
        return a + b*4
    
    a = 2
    b = 8
    c = next_even_fib(a, b)

    sum = a + b
    while c < limit:
        sum += c
        h = next_even_fib(b, c)
        b = c
        c = h
    return sum

print(sum_even_fib(MAX_VALUE))