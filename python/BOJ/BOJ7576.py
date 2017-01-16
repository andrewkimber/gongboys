test = 0

cols, rows = map(int, raw_input().split())

T = [[-1 for i in range(cols + 1)]]
for i in range(rows):
    tmp = [-1]
    row = raw_input()
    row = row.split(' ')[:cols]
    row = map(int, row)
    tmp += row
    T.append(tmp)


def adj(point):
    x = point[0]
    y = point[1]
    adjset = []
    if x > 1:
        if T[x - 1][y] == 0:
            adjset.append([x - 1, y])
    if x < rows:
        if T[x + 1][y] == 0:
            adjset.append([x + 1, y])
    if y > 1:
        if T[x][y - 1] == 0:
            adjset.append([x, y - 1])
    if y < cols:
        if T[x][y + 1] == 0:
            adjset.append([x, y + 1])
    return adjset


frontier = []
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if T[i][j] == 1:
            frontier.append([i, j])

day = 0
while frontier:
    day += 1
    new_frontier = []
    for point in frontier:
        for adj_point in adj(point):
            x = adj_point[0]
            y = adj_point[1]
            T[x][y] = 1
            new_frontier.append(adj_point)
    frontier = new_frontier

    if test:
        print "DAY " + str(day)
        print "new_frontier: " + str(frontier)
        for i in range(1, rows + 1):
            list = []
            for j in range(1, cols + 1):
                list.append(str(T[i][j]))
            print ' '.join(list)
        print "========="

if sum(map(lambda x: x.count(0), T)):
    print -1
else:
    print day - 1
