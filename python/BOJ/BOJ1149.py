color_dict = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

cost_list = []

numHouse = int(raw_input())

for i in range(numHouse):
    cost_list.append(map(int, raw_input().split()))


def cost(i, color):
    return cost_list[i][color]


def search_path(n):
    if n == 1:
        all_paths = []
        for i in range(3):
            all_paths.append([i])
        return all_paths
    else:
        new_list = []
        for path in search_path(n - 1):
            last_color = path[-1]
            for next_color in color_dict[last_color]:
                path_copy = path[:]
                path_copy += [next_color]
                new_list.append(path_copy)
        return new_list


all_paths = search_path(numHouse)

min_cost = None
for path in all_paths:
    cost = 0
    for i in range(len(path)):
        cost += cost(i, path[i])
    if min_cost is None:
        min_cost = cost
    if min_cost > cost:
        min_cost = cost
print min_cost
