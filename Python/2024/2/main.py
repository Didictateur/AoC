from parse import parse
from numpy import sign

# Partie 1
def isSafe(l: list[int]):
    """
    Retourne Vrai si et seulement si la liste donnée en entrée est monotone avec une évolution entre 1 et 3 entre chaque terme
    """
    # s'il y a un ou deux éléments, l'assertion est vraie
    if len(l) < 2:
        return True

    s = sign(l[1] - l[0]) # connaitre le sens de l'évolution
    for i in range(len(l) - 1):
        diff = l[i+1] - l[i]
        
        if sign(diff) != s: # non monotone
            return False

        if abs(diff) not in [1, 2, 3]: # contrainte non respectée
            return False

    return True

def part1(fileName: str):
    """
    Compte le nombre de lignes monotones et dont l'évolution est comprise entre 1 et 3
    """
    # récupère les données
    data = parse(fileName, integer=True)

    res = len([l for l in data if isSafe(l)]) # compte le nombre de ligne sécurisée
    return res


# Partie 2
def isSafe2(l: list[int]):
    """
    Retourne Vrai si et seulement si la liste donnée en entrée est quasi monotone avec une évolution entre 1 et 3 entre chaque terme
    """
    if isSafe(l): # si déjà sécurisée, renvoyer Vraie
        return True

    for i in range(len(l)):
        sous_liste = l[:i] + l[i+1:] # la sous-liste sans le i-ème élément
        if isSafe(sous_liste): # la sous-liste est sécurisée
            return True

    return False # aucune des sous-listes n'est sécurisée

def part2(fileName: str):
    """
    Compte le nombre de lignes quasi monotones et dont l'évolution est comprise entre 1 et 3
    """
    # récupère les données
    data = parse(fileName, integer=True)

    res = len([l for l in data if isSafe2(l)]) # compte le nombre de ligne sécurisée
    return res
