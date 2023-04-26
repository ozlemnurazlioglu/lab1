def sieve_of_eratosthenes(numbers):
    primes = [True] * len(numbers)

    for i in range(len(numbers)):
        if primes[i]:
            for j in range(i + numbers[i], len(numbers), numbers[i]):
                primes[j] = False

    result = [numbers[i] for i in range(len(numbers)) if primes[i]]

    return result
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10,13,20]
primes = sieve_of_eratosthenes(numbers)
print(primes)