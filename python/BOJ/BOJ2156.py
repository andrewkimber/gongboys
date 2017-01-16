N = int(raw_input())

wine = [0]*10001

for i in xrange(1,N+1):
    wine[i] = int(raw_input())


dp = {}
dp[1] = wine[1]
dp[2] = wine[1]+wine[2]
dp[3] = max(wine[1]+wine[2], wine[2]+wine[3], wine[3]+wine[1])

n = 4
while n <= N:
    result = max(dp[n-3] + wine[n - 1] + wine[n], dp[n-2] + wine[n], dp[n-1])
    dp[n] = result
    n += 1

print dp[N]
