def empty_row(L):
    l_row = []
    for i in range(len(L)):
        if not "#" in L[i]:
            l_row.append(i)
    return l_row

def empty_col(L):
    l_col= []
    for i in range(len(L[0])):
        if not "#" in [l[i] for l in L]:
            l_col.append(i)
    return l_col

def short(pos0, pos1, l_row, l_col, old_coef = 2):
    d = abs(pos1[0] - pos0[0])
    d += abs(pos1[1] - pos0[1])

    d += (old_coef-1)*len([x for x in range(min(pos0[0], pos1[0]), max(pos0[0], pos1[0])) if x in l_row])
    d += (old_coef-1)*len([x for x in range(min(pos0[1], pos1[1]), max(pos0[1], pos1[1])) if x in l_col])

    return d

## result1

def result1(L):
    L = [l[0] for l in L]

    l_row = empty_row(L)
    l_col = empty_col(L)

    L_galaxy = []
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "#":
                L_galaxy.append((i, j))

    s = 0
    for i in range(len(L_galaxy)):
        for j in range(i+1, len(L_galaxy)):
            s += short(L_galaxy[i], L_galaxy[j], l_row, l_col)

    return s

## restult2

def result2(L):
    L = [l[0] for l in L]

    l_row = empty_row(L)
    l_col = empty_col(L)

    L_galaxy = []
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "#":
                L_galaxy.append((i, j))

    s = 0
    for i in range(len(L_galaxy)):
        for j in range(i+1, len(L_galaxy)):
            s += short(L_galaxy[i], L_galaxy[j], l_row, l_col, 1000000)

    return s