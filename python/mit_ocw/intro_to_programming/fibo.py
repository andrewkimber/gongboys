global slowNumCall
global fastNumCall
slowNumCall=0
fastNumCall=0


def slowFibonaci(n):
    global slowNumCall
    slowNumCall += 1
    if n==1 or n==2:
        return 1
    else:
        return slowFibonaci(n-1)+slowFibonaci(n-2)


def fastFibonaci(n,memo={}):
    global fastNumCall
    fastNumCall +=1
    if n==1 or n==2:
        memo[n]=1
        return 1
    if n in memo:
        return memo[n]
    else:
        result= fastFibonaci(n-1)+fastFibonaci(n-2)
        memo[n]=result
        return result

def test(n):
    print slowFibonaci(n)
    print "slowFibonaci called", slowNumCall, "times"
    print "-------------------------------------"
    print fastFibonaci(n)
    print "fastFibonaci called", fastNumCall, "times"


test(35)