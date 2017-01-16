costs = [[0, 0, 0]]

numHouse = int(raw_input())

for house in range(numHouse):
    costs.append(map(int, raw_input().split()))

Dp = {}
Dp[(1, 0)] = costs[1][0]
Dp[(1, 1)] = costs[1][1]
Dp[(1, 2)] = costs[1][2]

for i in range(2, numHouse + 1):
    Dp[(i, 0)] = min(Dp[(i - 1, 1)], Dp[(i - 1, 2)])+costs[i][0]
    Dp[(i, 1)] = min(Dp[(i - 1, 0)], Dp[(i - 1, 2)])+costs[i][1]
    Dp[(i, 2)] = min(Dp[(i - 1, 0)], Dp[(i - 1, 1)])+costs[i][2]

result = min(Dp[(numHouse,0)], Dp[(numHouse,1)], Dp[(numHouse,2)])

print result
