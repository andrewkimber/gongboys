
num_rows = int(raw_input())

table = [[]]
Dp = [[]]
for i in xrange(1, num_rows + 1):
    tmp = raw_input()
    tmp = tmp.split(' ')[:i]
    tmp = map(lambda x: int(x), tmp)
    table.append(tmp)
    lst = [0 for j in xrange(i)]
    Dp.append(lst)

Dp[1][0] = table[1][0]

for i in xrange(2, num_rows + 1):
    for j in xrange(0, i):
        if j == 0:
            Dp[i][j] = Dp[i - 1][j] + table[i][j]
        elif j == i - 1:
            Dp[i][j] = Dp[i - 1][j - 1] + table[i][j]
        else:
            Dp[i][j] = max(Dp[i - 1][j - 1], Dp[i - 1][j]) + table[i][j]

result = 0
for i in xrange(num_rows):
    if Dp[num_rows][i] > result:
        result = Dp[num_rows][i]

print result
