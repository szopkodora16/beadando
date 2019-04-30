szam = 5000
primes = set(range(2,szam+1))

for p in range(2,szam+1):
    if p in primes:
        for i in range(2,szam+1):
            if p*i in primes:
                primes.remove(p*i)

print(primes)

