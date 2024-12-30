def parse_to_dico(L):
    dico = {}
    for l in L[1:]:
        c = (l[2][1:-1], l[3][:-1])
        dico[l[0]] = c
    return dico

## result1

def result1(L):
    instr = L[0][0]
    n = len(instr)
    d = parse_to_dico(L)

    step = 0
    i = 0
    here = "AAA"
    while here != "ZZZ":
        step += 1
        if instr[i%n] == "L":
            here = d[here][0]
        else:
            here = d[here][1]
        i += 1

    return step

## restult2

def has_finish(ghosts):
    for g in ghosts:
        if g[-1] != "Z":
            return False
    return True

def result2(L):
    instr = L[0][0]
    n = len(instr)
    d = parse_to_dico(L)

    ghosts = []
    for key in d.keys():
        if key[-1] == "A":
            ghosts.append(key)
    
    step = 0
    i = 0
    while not has_finish(ghosts):
        step += 1
        for g in ghosts:
            if instr[i%n] == "L":
                ghosts[ghosts.index(g)] = d[g][0]
            else:
                ghosts[ghosts.index(g)] = d[g][1]
        i += 1
    
    return step