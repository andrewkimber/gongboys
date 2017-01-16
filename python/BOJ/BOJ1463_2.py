N = int(raw_input(""))

dict = {}

dict[1] = 0
dict[2] = 1
dict[3] = 1

for i in range(4, N + 1):
    dict[i] = dict[i - 1] + 1
    if i % 2 == 0:
        dict[i] = min(dict[i], dict[i / 2] + 1)
    if i % 3 == 0:
        dict[i] = min(dict[i], dict[i / 3] + 1)

print dict[N]