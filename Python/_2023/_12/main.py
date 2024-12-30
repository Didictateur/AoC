def format_input(L):
    return [[l[0], [int(x) for x in (l[1].split(','))]] for l in L]

def is_valide(springs, L_springs):
    l = springs.split('.')
    l_nb = [len(l_) for l_ in l if l_ != '']
    return l_nb == L_springs

def test(tested_springs, undetermined_springs, L_springs):
    if undetermined_springs == "":
        if is_valide(tested_springs, L_springs):
            return 1
        return 0
    c = undetermined_springs[0]
    if c == "?":
        return test(tested_springs+".", undetermined_springs[1:], L_springs) + test(tested_springs+"#", undetermined_springs[1:], L_springs)
    else:
        return test(tested_springs+c, undetermined_springs[1:], L_springs)

## result1

def result1(L):
    L = format_input(L)

    s = 0
    for i in range(len(L)):
        s += test("", L[i][0], L[i][1])
    return s    
    
## restult2

def result2(L):
    pass