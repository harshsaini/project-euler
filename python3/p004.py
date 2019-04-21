"""
Problem 4 - Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is:
    9009 = 91 × 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse(n: int) -> int:
    reversed = 0
    while n > 0:
        reversed = (10*reversed) + (n % 10)
        n = int(n/10)
    return reversed


def is_palindrome(n: int) -> bool:
    return n == reverse(n)


def search() -> int:
    a = 999
    b = 999
    limit = 100
    largest_palindrome = -1
    while a > limit:
        while b > limit:
            value = a * b
            if is_palindrome(value):
                largest_palindrome = value if value > largest_palindrome else largest_palindrome
            b -= 1
        a -= 1
        b = a
    return largest_palindrome


print(search())
