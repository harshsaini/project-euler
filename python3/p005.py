"""
Problem 5 - Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
from typing import Dict
from common.primes import get_prime_factors, generate_primes


MAX_NUMBER = 20
MIN_NUMBER = 1

# Naive solution - using prime factorization and least common multipe approach to find the solution
factor_count: Dict[int, int] = {}
for n in range(MIN_NUMBER, MAX_NUMBER + 1):
    factors = get_prime_factors(n)
    
    local_counts: Dict[int, int] = {}
    for factor in factors:
        if factor not in local_counts:
            local_counts[factor] = 1
        else:
            local_counts[factor] += 1

    for factor in local_counts:
        if factor not in factor_count or factor_count[factor] < local_counts[factor]:
            factor_count[factor] = local_counts[factor]

result = 1
for factor in factor_count:
    result *= factor**(factor_count[factor])

print(result)

# Better solution (assuming generation of primes is cheaper than factorization given above)
result = 1
primes = generate_primes(MAX_NUMBER)
for prime in primes:
    curr_val = prime
    while not curr_val > MAX_NUMBER:
        prev_val = curr_val
        curr_val *= prime
    result *= prev_val

print(result)


# Optimal solution (assuming generation of primes is cheaper than factorization given above)
result = 1
primes = generate_primes(MAX_NUMBER)
for prime in primes:
    exponent = math.floor(
        math.log(MAX_NUMBER) / math.log(prime)
    )
    result *= prime ** exponent

print(result)