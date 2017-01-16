minimum, maximum = map(int,raw_input().split())


sieve = {}
for i in range(2, maximum + 1):
    sieve[i] = 0

for i in range(2, maximum + 1):
    if sieve[i] == 0:
        n = 2
        while i * n < maximum + 1:
            sieve[i * n] = 1
            n += 1

for i in range(2, maximum + 1):
    if sieve[i] == 0 and i >= minimum:
        print i