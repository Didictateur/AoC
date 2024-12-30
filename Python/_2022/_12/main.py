import os

def char_to_int(c:str):
    letters = "SabcdefghijklmnopqrstuvwxyzE"
    for i in range(len(letters)):
        if letters[i] == c:
            return i
    return None

def to_dico(L):
    n = len(L)
    m = len(L[0])
    dico = {}

    for i in range(n-1):
        for j in range(m):
            if abs(char_to_int(L[i][j])-char_to_int(L[i+1][j])) <= 1:
                if (i, j) in dico:
                    dico[(i, j)].append((i+1, j))
                else:
                    dico[(i, j)] = [(i+1, j)]
                if (i+1, j) in dico:
                    dico[(i+1, j)].append((i, j))
                else:
                    dico[(i+1, j)] = [(i, j)]

    for i in range(n):
        for j in range(m-1):
            if abs(char_to_int(L[i][j])-char_to_int(L[i][j+1])) <= 1:
                if (i, j) in dico:
                    dico[(i, j)].append((i, j+1))
                else:
                    dico[(i, j)] = [(i, j+1)]
                if (i, j+1) in dico:
                    dico[(i, j+1)].append((i, j))
                else:
                    dico[(i, j+1)] = [(i, j)]
    return dico

def find_start(L):
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "S":
                return (i, j)

def current_min(values, L_current: list[tuple[int, int]]):
    pos = L_current[0]
    m = values[pos[0]][pos[1]]
    for p in L_current:
        if m > values[pos[0]][pos[1]]:
            m = values[pos[0]][pos[1]]
            pos = p
    return pos

def Dikjstra(dico, L):

    values = []
    for i in range(len(L)):
        values.append([0]*len(L[0]))
    L_current = [find_start(L)]
    dead = []

    while L_current:
        pos = current_min(values, L_current)

        # os.system("clear")
        # txt = ""
        # for i in range(len(L)):
        #     for j in range(len(L[0])//2):
        #         if (i, j) in dead:
        #             txt += f"{values[i][j]} "
        #         elif (i, j) == pos:
        #             txt += "X "
        #         elif (i, j) in L_current:
        #             txt += "x "
        #         else:
        #             txt += f"{L[i][j]} "
        #     txt += '\n'
        # print(txt)
        # input()

        if L[pos[0]][pos[1]] == "E":
            return values[pos[0]][pos[1]]
        print(L[pos[0]][pos[1]], pos)
        L_current = [cur for cur in L_current if not cur==pos]
        l_neigh = dico[pos]
        for neigh in [neigh for neigh in l_neigh if not neigh in dead]:
            if neigh in L_current:
                values[neigh[0]][neigh[1]] = min(values[neigh[0]][neigh[1]], values[pos[0]][pos[1]]+1)
            else:
                values[neigh[0]][neigh[1]] = values[pos[0]][pos[1]]+1
                L_current.append(neigh)
        dead.append(pos)

## result1

def result1(L):
    dico = to_dico([l[0] for l in L])
    return Dikjstra(dico, [l[0] for l in L])
    
## result2

def result2(L):
    pass