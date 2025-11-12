def parse(
        fileName: str,
        integer: bool = False,
        liste: bool = False,
        texte: bool = False
    ):
    # lecture du fichier
    with open(fileName, "r") as f:
        if texte:
            with open(fileName, "r") as f:
                return f.read()
        else:
            L = []
            # éclater chaque line en liste
            for line in [line.split() for line in f.readlines() if line.split() != []]:
                # si ce sont des entiers
                if integer:
                    L.append([int(x) for x in line]) # changer en entier
                # sinon ne rien faire
                else:
                    L.append(line)

            # si une liste est attendue, chaque ligne n'a qu'un seu élément
            if liste:
                L = [line[0] for line in L]
        return L
