# this algorithm uses bottom-up approach, incrementing the length of the subsets by 1 each loop.

num_tests = int(raw_input())


def run():
    num_file = int(raw_input())

    A = {0:0}
    Asum = {0:0}
    temp = raw_input()
    temp = temp.split(' ')[:num_file]
    for i in range(len(temp)):
        Asum[i+1] = Asum[i] + int(temp[i])
        A[i+1] = (int(temp[i]))

    Dp = {}
    for i in xrange(1, num_file + 1):
        Dp[(i, i)] = A[0]

    for length in xrange(2, num_file + 1):
        for i in xrange(1, num_file - length + 2):
            j = i + length - 1
            Dp[(i, j)] = 10001
            for k in xrange(i, j):
                cost = Dp[(i, k)] + Dp[(k + 1, j)] + Asum[j] - Asum[i-1]
                if cost < Dp[(i, j)]:
                    Dp[(i, j)] = cost
    return Dp[(1, num_file)]


for i in range(num_tests):
    print run()

