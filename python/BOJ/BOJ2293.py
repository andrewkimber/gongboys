a = raw_input("")

num_coins = int(a.split(" ")[0])
k = int(a.split(" ")[1])

coin = []
for i in range(num_coins):
    coin.append(int(raw_input("")))

cache = []
for i in range(k+1):
    cache.append(0)

cache[0] = 1


# 동전#1만으로 할 수 있는 경우의수 + 동전#1&#2만으로 할 수 있는 경우의수 + 동전#1,2,3만으로 할 수 있는 경우의수 + ... + 모든 동전으로 할 수 있는 경우의 수
for i in range(num_coins):
    for j in range(1, k+1):
        if j >= coin[i]:
            cache[j] += cache[j-coin[i]]

print cache[k]
