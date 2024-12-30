import math

def possible_scores(time, record):
    return len([t*(time-t) for t in range(time+1) if t*(time-t) > record])

## result1

def result1(L):
    s = 1
    for i in range(len(L[0])):
        s *= possible_scores(L[0][i], L[1][i])
    return s

## restult2

def result2(L):
    time = 0
    record = 0
    for i in range(len(L[0])):
        t = L[0][i]
        r = L[1][i]
        time = time*10**int(math.log(t, 10)+1)+t
        record = record*10**int(math.log(r, 10)+1)+r
    return possible_scores(time, record)