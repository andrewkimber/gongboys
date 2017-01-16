def fibonacci(n, memo={}):
    if n == 0:
        memo[0] = 0
        return 0
    if n == 1:
        memo[n] = 1
        return 1
    if n in memo:
        return memo[n]
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        memo[n] = result
        return result

N = int(raw_input(""))

for i in range(N):
    n = int(raw_input(""))
    if n == 0:
        print '1 0'
    else:
        print str(fibonacci(n-1)) + ' ' + str(fibonacci(n))