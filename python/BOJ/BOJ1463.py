N = int(input(""))
level = {1: 0}

i = 1
frontier = [1]
while N not in frontier:
    next = []
    for u in frontier:
        for v in [u + 1, 2 * u, 3 * u]:
            if v <= N:
                if v not in level:
                    level[v] = i
                    next.append(v)
    frontier = next
    i += 1

print level[N]

