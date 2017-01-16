from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction


def nCk(n, k):
    return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

num = int(raw_input())

memo = {}


# bottom-up style DP. Will work for input 1000, unlike the following recursion style DP.
def catalan_bu(num):
    for i in xrange(num+1):
        if i <= 1:
            memo[i] = 1
        else:
            f = 0
            for j in xrange(i):
                f += memo[j]*memo[i-j-1]
            memo[i] = f
    return memo[num]


# recursion style DP. Will break for input 1000, by stack overflow.
def catalan_recur(num,memoize={}):
    if num in memoize:
        return memoize[num]
    if num <= 1:
        memoize[num] = 1
        return memoize[num]
    else:
        result = 0
        for i in range(num):
            result += catalan_recur(i,memoize) * catalan_recur(num-i-1,memoize)
        memoize[num] = result
        return result


def catalan_math(num):
    return nCk(2*num,num)/(1+num)


# if the input is 1000, bottom-up style will work, but recursion style will break with stack overflow

# print catalan_math(num)

# print catalan_bu(num)

print catalan_recur(num)
