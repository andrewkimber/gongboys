rows, cols = map(int, raw_input().split())

heights = [[0] * (cols + 1)]
for i in xrange(rows):
    mapped_cs = map(int, raw_input().split())
    temp = [0]
    temp += mapped_cs
    heights.append(temp)


def adj(point):
    x, y = point[0], point[1]
    result = []
    if x < rows:
        if heights[x][y] > heights[x + 1][y]:
            result.append((x + 1, y))
    if x > 1:
        if heights[x][y] > heights[x - 1][y]:
            result.append((x - 1, y))
    if y < cols:
        if heights[x][y] > heights[x][y + 1]:
            result.append((x, y + 1))
    if y > 1:
        if heights[x][y] > heights[x][y - 1]:
            result.append((x, y - 1))
    return result


def search(point, memo={}):
    if point in memo:
        return memo[point]

    if point == (rows, cols):
        f = 1
        memo[point] = 1
    else:
        f = 0
        for adj_points in adj(point):
            f += search(adj_points, memo)
        memo[point] = f
    return f

print search((1, 1))