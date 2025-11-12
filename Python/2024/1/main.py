from parse import parse

# Partie 1
def part1(fileName: str):
    """
    Compare deux listes de nombre en sommant la différence entre les éléments triés et retourne le résultat
    """
    # parse les données sous forme de tableau
    data = parse(fileName, integer=True)

    L1 = [l[0] for l in data] # la première colonne
    L2 = [l[1] for l in data] # la deuxième colonne

    # tri les listes
    L1.sort()
    L2.sort()

    res = 0
    for i in range(len(L1)):
        res += abs(L1[i] - L2[i]) # différence entre les termes

    return res

# Partie 2
def part2(fileName: str):
    """
    Compare deux listes de nombres calculant un score. Ce score correspond à la somme des éléments de gauche, multiplié par leur occurence dans leur seconde liste
    """
    # parse les données sous forme de tableau
    data = parse(fileName, integer=True)

    L1 = [l[0] for l in data] # la première colonne
    L2 = [l[1] for l in data] # la deuxième colonne

    res = 0
    for i in range(len(L1)):
        nb = L1[i] # le terme
        occ = len([n for n in L2 if n == nb]) # son nombre d'occurence

        res += nb * occ # mettre à jour le résultat
        
    return res
