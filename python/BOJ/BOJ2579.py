N = int(raw_input(""))

stair=[0]
for i in range(N):
    cost = int(raw_input(""))
    stair.append(cost)


def Dp(i,memo={}):
    if i == 0:
        memo[0] = 0
        return 0
    if i == 1:
        memo[1] = stair[1]
        return stair[1]
    if i == 2:
        memo[2] = stair[2] + stair[1]
        return stair[2] + stair[1]
    if i in memo:
        return memo[i]
    else:
        cost = max(Dp(i-2, memo)+stair[i], Dp(i-3, memo)+stair[i-1]+stair[i])
        memo[i] = cost
        return cost

print Dp(N)