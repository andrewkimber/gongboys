rows, cols = map(int, raw_input().split())

heights =[]
for i in xrange(rows):
    mapped_cs = map(int, raw_input().split())
    heights.append(mapped_cs)

Dp = [[0 for i in range(cols)] for j in range(rows)]
Dp[rows-1][cols-1] = 1


def adj(point):
    x, y = point[0], point[1]
    result = []
    if x < rows-1:
        if heights[x][y] < heights[x + 1][y]:
            result.append((x + 1, y))
    if x > 0:
        if heights[x][y] < heights[x - 1][y]:
            result.append((x - 1, y))
    if y < cols-1:
        if heights[x][y] < heights[x][y + 1]:
            result.append((x, y + 1))
    if y > 0:
        if heights[x][y] < heights[x][y - 1]:
            result.append((x, y - 1))
    return result


frontier = [[rows-1,cols-1]]
visited = [[rows-1,cols-1]]
while frontier:
    new_frontier = []
    for point in frontier:
        x = point[0]
        y= point[1]
        for uphill in adj(point):
            _x = uphill[0]
            _y = uphill[1]
            Dp[_x][_y] += Dp[x][y]
            if uphill in visited:

            if uphill not in visited:
                visited.append(uphill)
                new_frontier.append(uphill)
    frontier = new_frontier

for i in range(rows):
    print ' '.join(map(str,Dp[i]))
