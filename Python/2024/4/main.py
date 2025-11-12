from parse import parse

def part1(fileName: str):
    """
    Compte le nombre d'apparition du mot "XMAS"
    """
    # récupérer les données
    data = parse(fileName, liste=True)

    # toutes les directions possibles
    direction = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if (di, dj) != (0, 0):
                direction.append([di, dj])

    res = 0
    # parcourir le tableau pour trouver le mot
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "X": # on a trouvé la première lettre
                for (di, dj) in direction:
                    # vérifier si le mot analysé ne dépasse pas du tableau
                    if i+3*di in range(len(data)) and j+3*dj in range(len(data[0])):
                        # former le mot analysé
                        mot = ""
                        for k in range(4):
                            mot += data[i + k*di][j + k*dj]
                        # si le mot est "XMAS" !
                        if mot == "XMAS":
                            res += 1
    return res

def part2(fileName: str):
    """
    Compte le nombre d'apparition de X-MAS en forme de croix
    """
    # récupération des données
    data = parse(fileName, liste=True)

    res = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] == "A": # peut être le centre d'un X-MAS
                nb_M = 0
                nb_S = 0
                # regarder les diagonales
                for (di, dj) in [(1, 1), (1, -1), (-1, 1) , (-1, -1)]:
                    letter = data[i+di][j+dj]
                    if letter == "S":
                        nb_S += 1
                    if letter == "M":
                        nb_M += 1
                    if nb_M == 2 and nb_S == 2: # X-MAS trouvé !
                        if data[i+1][j+1] != data[i-1][j-1]: # pas de MAM/SAS
                            res += 1
    return res
