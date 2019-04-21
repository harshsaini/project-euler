import math
from typing import List, Set


def get_prime_factors(number: int) -> List[int]:
    """
        Get all prime factors for a given number
    """
    factors = [1]
    n = number

    def factorize_with(k: int, factor: int)-> int:
        while k % factor == 0:
            k = k / factor
            factors.append(factor)
        return k

    current_factor = 2
    previous_factor = 1

    # manual calculation for 2
    n = factorize_with(n, current_factor)
    current_factor = current_factor + 1

    # search from 3 onwards
    limit = int(math.sqrt(n)) + 1
    while current_factor < limit:
        n = factorize_with(n, current_factor)
        current_factor += 2

    if len(factors) == 1:
        factors.append(n)

    return factors


def generate_primes(limit: int, window_size: int = 1000) -> Set[int]:
    primes = set()

    if limit > 2:
        primes.add(2)

    prime_counters: Dict[int, int] = {2: 2}

    def generate_window(start: int, end: int) -> Set[int]:
        return set(range(start, end + 1))

    def get_multiples_in_window(prime: int, curr_value: int, max_value: int) -> Set[int]:
        multiples = set()
        
        while not curr_value > max_value:
            multiples.add(curr_value)
            curr_value += prime
        
        return multiples

    def sieve(window: Set[int], window_max_value: int):
        window = window - primes

        while window:
            for prime in prime_counters:
                window = window - get_multiples_in_window(prime, prime_counters[prime], window_max_value)
            if window:
                next_prime = window.pop()
                primes.add(next_prime)
                prime_counters[next_prime] = next_prime

    n = 3
    while n < limit:
        start = n
        end = window_size + n if limit > (window_size + n) else limit
        n = end

        window = generate_window(start, end)
        sieve(window, end)

    return primes
        
