# by Changhyun Ryu... still Runtime Error...

rc = raw_input()
rows = int(rc.split(" ")[0])
cols = int(rc.split(" ")[1])

heights = [[0] * (cols + 1)]
for i in range(rows):
    cs = raw_input()
    mapped_cs = map(lambda x: int(x), cs.split(' ')[:cols])
    temp = [0]
    temp += mapped_cs
    heights.append(temp)


def make():
    return [[0, 0], [0, 0]]


result_map = []
for t in range(0, rows + 1):
    tmp = []
    for tt in range(0, cols + 1):
        tmp += [make()]
    result_map += [tmp]

result_map[1][1][0][0] = 1


def sum_tile(tile_x, tile_y):
    tile = result_map[tile_x][tile_y]
    return tile[0][0] + tile[0][1] + tile[1][0] + tile[1][1]


# def print_arr():
#     print('============')
#     for _x in range(1, rows + 1):
#         for _y in range(1, cols + 1):
#             print(sum_tile(_x, _y), end=' ')
#         print('\n')


def add(_point):
    _x, _y = _point[0], _point[1]
    _next_set = set()
    if result_map[_x][_y] == 0:
        return _next_set

    if _x < rows:
        if heights[_x + 1][_y] < heights[_x][_y]:
            if result_map[_x + 1][_y][0][1] < sum_tile(_x, _y):
                result_map[_x + 1][_y][0][1] = sum_tile(_x, _y)
                _next_set.add((_x + 1, _y))
    if _x > 1:
        if heights[_x - 1][_y] < heights[_x][_y]:
            if result_map[_x - 1][_y][1][0] < sum_tile(_x, _y):
                result_map[_x - 1][_y][1][0] = sum_tile(_x, _y)
                _next_set.add((_x - 1, _y))
    if _y < cols:
        if heights[_x][_y + 1] < heights[_x][_y]:
            if result_map[_x][_y + 1][0][0] < sum_tile(_x, _y):
                result_map[_x][_y + 1][0][0] = sum_tile(_x, _y)
                _next_set.add((_x, _y + 1))
    if _y > 1:
        if heights[_x][_y - 1] < heights[_x][_y]:
            if result_map[_x][_y - 1][1][1] < sum_tile(_x, _y):
                result_map[_x][_y - 1][1][1] = sum_tile(_x, _y)
                _next_set.add((_x, _y - 1))
    return _next_set


next_set = [(1, 1)]

while len(next_set) != 0:
    loop_range = sorted(next_set)
    next_set = set()
    # print(loop_range)
    # print_arr()
    for point in loop_range:
        next_set |= add(point)

print(sum_tile(rows, cols))