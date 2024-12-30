def get_dico(L):
    dico = {}
    for a, b in L:
        if a in dico:
            dico[a].append(b)
        else:
            dico[a] = [b]
        
        if b in dico:
            dico[b].append(a)
        else:
            dico[b] = [a]
    return dico

def count_path(dico, pos, dead) -> int:
    if pos == "end":
        return 1
    neig = [p for p in dico[pos] if not p in dead]
    s = 0
    for ne in neig:
        if pos[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s += count_path(dico, ne, dead)
        else:
            s += count_path(dico, ne, dead+[pos])
    return s

def count_path_twice(dico, pos, dead, used=False) -> int:
    if pos == "end":
        return 1
    neig = dico[pos]
    s = 0
    for ne in neig:
        if not ne in dead and pos[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s += count_path_twice(dico, ne, dead, used)
        elif not ne in dead:
            s += count_path_twice(dico, ne, dead+[pos], used)
        elif not used and not ne in {"start", "end"}:
            if pos[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                s += count_path_twice(dico, ne, dead, True)
            else:
                s += count_path_twice(dico, ne, dead+[pos], True)
    return s

## result1

def result1(L):
    L = [l[0].split('-') for l in L]
    dico = get_dico(L)

    return count_path(dico, "start", [])
    
## result2

def result2(L):
    L = [l[0].split('-') for l in L]
    dico = get_dico(L)

    return count_path_twice(dico, "start", [], False)