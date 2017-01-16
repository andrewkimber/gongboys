N = int(raw_input(""))
D = []
for i in range(N):
    D.append([0]*10)

for i in range(10):
    D[0][i]=1

for n in range(1,N):
    for j in range(10):
        if j >= 1:
            D[n][j] += D[n-1][j-1]
        if j <= 8:
            D[n][j] += D[n-1][j+1]


total = 0
for i in range(1, 10):
    total += D[N-1][i]


print total % 1000000000


# if you want the actual step_numbers(not the num of step_numbers), then the below code should work.
# frontier = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 1
#
# while n < N:
#     next = []
#     for i in frontier:
#         last_num = i % 10
#         if last_num == 0:
#             next.append(i * 10 + 1)
#         elif last_num == 9:
#             next.append(i * 10 + 8)
#         else:
#             next.append(i * 10 + last_num + 1)
#             next.append(i * 10 + last_num - 1)
#     frontier = next
#     n += 1
#
# print frontier




