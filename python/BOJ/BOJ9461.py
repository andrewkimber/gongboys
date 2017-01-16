P = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2}

for i in range(6, 1001):
    p = P[i - 1] + P[i - 5]
    P[i] = p

N_tests = int(raw_input())
for i in range(N_tests):
    print P[int(raw_input())]