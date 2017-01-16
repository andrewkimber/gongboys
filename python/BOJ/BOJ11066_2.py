# this algorithm uses recursion, using substrings

maxnum = 10001

num_trial = int(raw_input())
for i in range(num_trial):
    Dp = [[maxnum for i in range(501)] for j in range(501)]
    sum = [0 for i in range(501)]

    num_file = int(raw_input())
    temp = raw_input()
    temp = temp.split(' ')
    for i in range(len(temp)):
        sum[i+1] = sum[i] + int(temp[i])


    def solve(start, end):
        p = Dp[start][end]
        if p != maxnum:
            return p
        if start == end:
            Dp[start][end] = 0
            return Dp[start][end]
        for i in range(start, end):
            if solve(start, i) + solve(i + 1, end) + sum[end] - sum[start-1] < p:
               p = solve(start, i) + solve(i + 1, end) + sum[end] - sum[start-1]
        Dp[start][end] = p
        return p

    print solve(1,num_file)
