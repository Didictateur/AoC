import os
import random as rd
import numpy as np

def list_to_dico(L):
    dico = {}
    n = len(L)
    m = len(L[0])
    for i in range(n):
        for j in range(m):
            l = neigh((i, j), (n ,m))
            ln = []
            for x, y in l:
                ln.append(((x, y), L[x][y]))
            dico[(i, j)] = ln
    return dico
    
def neigh(pos: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = pos
    n, m = end
    L = []
    for e in {-1, 1}:
        if 0 <= x+e and x+e < n:
            L.append((x+e, y))
        if 0 <= y+e and y+e < m:
            L.append((x, y+e))
    return L

def actual_min(values, L_actual) -> tuple[int, int]:
    pos = L_actual[0]
    m = values[pos[0]][pos[1]]
    for x, y in L_actual:
        if values[x][y] < m:
            m = values[x][y]
            pos = (x, y)
    return pos

def search(dico, end):
    n, m = end
    values = []
    for i in range(n):
        values.append([0]*m)

    dead = []
    L_actual = [(0, 0)]

    while L_actual:
        x, y = actual_min(values, L_actual)
        L_actual = [pos for pos in L_actual if pos != (x, y)]
        nb = dico[(x, y)]
        for pos, cost in nb:
            if pos in dead:
                pass
            elif pos in L_actual:
                values[pos[0]][pos[1]] = min(values[pos[0]][pos[1]], values[x][y]+cost)
            else:
                values[pos[0]][pos[1]] = values[x][y]+cost
                L_actual.append(pos)
        dead.append((x, y))

    return values[-1][-1]

def extand_right(L, m: int):
    for i in range(len(L)):
        l = L[i][-m:].copy()
        for x in l:
            L[i].append(max(1, (x+1)%10))

def extand_down(L, n: int):
    N = len(L)
    for i in range(N-n, N):
        l = [max(1, (x+1)%10) for x in L[i]]
        L.append(l)

def extand(L):
    n = len(L)
    m = len(L[0])

    for i in range(4):
        extand_right(L, m)
        extand_down(L, n)

## result1

def result1(L):
    L = [[int(x) for x in str(l[0])] for l in L]
    n = len(L)
    m = len(L[0])

    dico = list_to_dico(L)

    return search(dico, (n, m))

## restult2

def result2(L):
    L = [[int(x) for x in str(l[0])] for l in L]
    n = len(L)
    m = len(L[0])

    extand(L)
    print("extanded")

    dico = list_to_dico(L)

    return search(dico, (5*n, 5*m))