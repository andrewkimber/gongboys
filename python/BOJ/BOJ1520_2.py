import sys

rows = 500
cols = 500
heights=[]
for i in xrange(1000,500,-1):
    list = [j for j in range(i, i - 500, -1)]
    heights.append(list)

sys.setrecursionlimit(1500)

# returns the adjacent points
def adj(point):
    x, y = point[0], point[1]
    result = []
    if x < rows-1:
        if heights[x][y] > heights[x + 1][y]:
            result.append((x + 1, y))
    if x > 0:
        if heights[x][y] > heights[x - 1][y]:
            result.append((x - 1, y))
    if y < cols-1:
        if heights[x][y] > heights[x][y + 1]:
            result.append((x, y + 1))
    if y > 0:
        if heights[x][y] > heights[x][y - 1]:
            result.append((x, y - 1))
    return result


# DFS with memoization
def search(point, memo={}):
    if point in memo:
        return memo[point]

    if point == (rows-1, cols-1):
        f = 1
        memo[point] = 1
    else:
        f = 0
        for adj_points in adj(point):
            f += search(adj_points, memo)
        memo[point] = f
    return f

memo = {}
print search((0, 0))

# # visualizing the search map...
# for i in range(1, rows + 1):
#     string = ''
#     for j in range(1, cols + 1):
#         if (i, j) in memo:
#             string += str(memo[(i, j)]) + " "
#         else:
#             string += "x "
#     print string
