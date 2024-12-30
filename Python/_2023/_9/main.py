def interpolate(L: list[int]) -> list[int]:
    if [x for x in L if x != 0] == []:
        return L+[0,0]
    
    l = []
    for i in range(len(L)-1):
        l.append(L[i+1]-L[i])
    dl = interpolate(l)
    L.append(L[-1]+dl[-1])
    L = [L[0]-dl[0]] + L
    return L

## result1

def result1(L):
    s = 0
    for l in L:
        s += interpolate(l)[-1]
    return s

## restult2

def result2(L):
    s = 0
    for l in L:
        s += interpolate(l)[0]
    return s