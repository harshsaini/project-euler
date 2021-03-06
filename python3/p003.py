"""
Problem 3 - Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math
from typing import List

from common.primes import get_prime_factors

NUMBER = 600851475143


# def get_prime_factors(n: int) -> List[int]:
#     factors: List[int] = [1]

#     current_factor = 2
#     previous_factor = 1

#     limit = int(math.sqrt(n)) + 1
#     while current_factor < limit:
#         while n % current_factor == 0:
#             n = n / current_factor
#             factors.append(current_factor)
#             previous_factor = current_factor
#         current_factor = current_factor + (1 if current_factor == 2 else 2)
#     return factors

def get_largest_prime_factor(n: int) -> int:
    factors = get_prime_factors(n=n)
    return max(factors)

print(get_largest_prime_factor(n=NUMBER))
