from math import *

dico = {
    "|": ((1, 0), (-1, 0)),
    "-": ((0, 1), (0, -1)),
    "L": ((0, 1), (-1, 0)),
    "J": ((-1, 0), (0, -1)),
    "7": ((0, -1), (1, 0)),
    "F": ((1, 0), (0, 1)),
    ".": ((0, 0), (0, 0)),
}

def find_S(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == "S":
                return (i, j)
    raise Exception("No S in the list")

def get_next(pos, dir: str):
    x, y = pos
    L = []
    for (dx, dy) in dico[dir]:
        L.append((x + dx, y + dy))
    return L

## result1

def result1(L):
    L = [l[0] for l in L]
    xs, ys = find_S(L)
    next = (-1, -1)

    if (xs, ys) in get_next((xs+1, ys), L[xs+1][ys]):
        next = (xs+1, ys)
    elif (xs, ys) in get_next((xs-1, ys), L[xs-1][ys].lower()):
        next = (xs-1, ys)
    elif (xs, ys) in get_next((xs, ys+1), L[xs][ys+1]):
        next = (xs, ys+1)
    elif (xs, ys) in get_next((xs, ys-1), L[xs][ys-1]):
        next  = (xs, ys-1)
    else:
        raise Exception("No next")
    
    visited = [(xs, ys)]
    count = 0
    xs, ys = next
    while not (xs, ys) in visited:
        visited.append((xs, ys))
        next = get_next((xs, ys), L[xs][ys])
        if not next[0] in visited:
            xs, ys = next[0]
        else:
            xs, ys = next[1]
        count += 1
    return (count+1)//2

## restult2

def result2(L):
    L = [l[0] for l in L]
    xs, ys = find_S(L)
    next = (-1, -1)

    if (xs, ys) in get_next((xs+1, ys), L[xs+1][ys]):
        next = (xs+1, ys)
    elif (xs, ys) in get_next((xs-1, ys), L[xs-1][ys].lower()):
        next = (xs-1, ys)
    elif (xs, ys) in get_next((xs, ys+1), L[xs][ys+1]):
        next = (xs, ys+1)
    elif (xs, ys) in get_next((xs, ys-1), L[xs][ys-1]):
        next  = (xs, ys-1)
    else:
        raise Exception("No next")
    
    L_next = []
    for i in range(len(L)):
        L_next.append([(0, 0)]*len(L[0]))
    
    visited = [(xs, ys)]
    L_next[xs][ys] = next
    xs, ys = next
    while not (xs, ys) in visited:
        visited.append((xs, ys))
        next = get_next((xs, ys), L[xs][ys])
        if not next[0] in visited:
            L_next[xs][ys] = next[0]
            xs, ys = next[0]
        else:
            L_next[xs][ys] = next[1]
            xs, ys = next[1]
    
    s = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L_next[i][j] == (0, 0):
                x, y = i-1, j
                outside = True
                frontier = ""
                while x >= 0:
                    if L_next[x][y] != (0, 0):
                        match L[x][y] :
                            case "-":
                                outside = not outside
                            case "L":
                                frontier = "L"
                            case "J":
                                frontier = "J"
                            case "7":
                                if frontier == "L":
                                    outside = not outside
                                frontier = ""
                            case "F":
                                if frontier == "J":
                                    outside = not outside
                                frontier = ""
                    x -= 1
                s += int(not outside)

    return s