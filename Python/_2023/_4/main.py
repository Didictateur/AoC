## result1

def result1(L):
    score = 0
    for l in L:
        s = 1
        tirage = []
        winning = True
        for i in range(2, len(l)):
            if l[i] == '|':
                winning = False
            else:
                if winning:
                    tirage.append(l[i])
                else:
                    if l[i] in tirage:
                        s *= 2
        score += s//2
    return score

## restult2

def win_nb_copy(l):
    s = 0
    tirage = []
    winning = True
    for i in range(2, len(l)):
        if l[i] == '|':
            winning = False
        else:
            if winning:
                tirage.append(l[i])
            else:
                if l[i] in tirage:
                    s += 1
    return s

def result2(L):
    total = 0
    cards = [1]*len(L)
    indexes = [i for i in range(len(cards)) if cards[i] != 0]
    while indexes:
        index = indexes[0]
        nb = win_nb_copy(L[index])
        for i in [index+e+1 for e in range(nb)]:
            cards[i] += cards[index]
        total += cards[index]
        cards[index] = 0
        indexes = [i for i in range(len(cards)) if cards[i] != 0]
    return total
