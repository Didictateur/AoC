def has_symbole(i, j, N, M, L):
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if 0 <= i+di < N and 0 <= j+dj < M:
                if (not L[i+di][j+dj].isdigit()) and (L[i+di][j+dj] != "."):
                    return True
    return False

## result1

def result1(L):
    L = [l[0] for l in L]
    N = len(L)
    M = len(L[0])
    s = 0
    count = False
    for i in range(N):
        n = 0
        for j in range(M):
            if L[i][j].isdigit():
                n = 10*n+int(L[i][j])
                if has_symbole(i, j, N, M, L):
                    count = True
            else:
                if count:
                    s += n
                n = 0
                count = False
        if n != 0 and count:
            s += n
    return s

## restult

def more_then_two(l):
    l_ = [l[0][0]]
    for x in l:
        if x[0] not in l_:
            l_.append(x[0])
    return len(l_) > 2

def result2(L):
    s = 0
    L = [l[0] for l in L]
    Lc = []
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "*":
                Lc.append([])
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i+di < len(L) and 0 <= j+dj < len(L[0]):
                            if L[i+di][j+dj].isdigit():
                                Lc[-1].append((i+di, j+dj))
    lrepr = []
    for i in range(len(Lc)):
        l = Lc[i]
        if len(l) > 2:
            if not more_then_two(l):
                try:
                    l_ = [l[0]]
                    i = 0
                    while l[0][0] == l[i][0]:
                        i += 1
                    l_.append(l[i])
                    lrepr.append(l_)
                except:
                    pass
        elif len(l)==2:
            if abs(l[0][1]-l[1][1]) != 1:
                lrepr.append(l)

    for c in lrepr:
        x, y = c[0]
        w1 = L[x][y]

        e = 1
        while y-e >= 0 and L[x][y-e].isdigit():
            w1 = L[x][y-e]+w1
            e += 1
        e = 1
        while y+e < len(L[0]) and L[x][y+e].isdigit():
            w1 = w1+L[x][y+e]
            e += 1
        
        x, y = c[1]
        w2 = L[x][y]
        e = 1
        while y-e >= 0 and L[x][y-e].isdigit():
            w2 = L[x][y-e]+w2
            e += 1
        e = 1
        while y+e < len(L[0]) and L[x][y+e].isdigit():
            w2 = w2+L[x][y+e]
            e += 1

        s += int(w1)*int(w2)

    return s