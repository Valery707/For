numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
notprimes = []
for i in numbers[1:]:
    is_prime = 0
    for j in numbers[1:i]:
        if i % j == 0:
            is_prime += 1
            if is_prime > 1:
                notprimes.append(i)
                break
        if i == j:
            primes.append(i)
print('primes:', primes)
print('notprimes:',notprimes)

