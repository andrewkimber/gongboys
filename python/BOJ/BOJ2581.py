mn = int(raw_input())
mx = int(raw_input())

prime = {}
for i in range(2,mx+1):
    prime[i] = 0

result = []
sum = 0
for i in range(2,mx+1):
    if prime[i] == 0:
        n = 2
        while i * n <= mx:
            prime[i * n] = 1
            n += 1
        if mn <= i <= mx:
            result.append(i)
            sum += i


if sum == 0:
    print -1
else:
    print sum
    print result[0]