numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
k = 0
m = 0
primes = []
not_primes = []
for i in  numbers:
    if i == 1:
        continue
    if i == 2:
        primes.append(i)
        k += 1
        continue
    j = 1
    while j + 1 < i:
        j = j + 1
        if i % j:
            if j + 1 == i:
                primes.append(i)
                k += 1
            continue
        else:
            not_primes.append(i)
            m += 1
            break
print('Primes: ', primes)
print('Not primes: ', not_primes)


