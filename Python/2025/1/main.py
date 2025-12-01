from parse import parse

# Partie 1
def part1(fileName: str):
    '''
    Compte le nombre de fois qu'un verrou s'arrête sur le chiffre 0 étant donné une suite d'instruction
    '''

    # fonctions auxiliaires
    def R(n: int, delta: int):
        '''
        incrémente n de delta modulo 100 et retourne le résultat
        '''
        return (n + delta) % 100

    def L(n: int, delta: int):
        '''
        décrémente n de delta modulo 100 et retourne le résultat
        '''
        return (n - delta) % 100

    # corps de la fonction
    instructions = parse(fileName, liste=True)
    
    res = 0
    n = 50
    for instr in instructions:
        if instr != "" and instr[0] == 'R': # décalage vers la droite
            n = R(n, int(instr[1:]))
        elif instr != "" and instr[0] == 'L': # décalage vers la gauche
            n = L(n, int(instr[1:]))
        else:
            continue # instruction invalide
        res += int(n == 0) # incrémente si on est à 0

    return res

# Partie 2
def part2(fileName: str):
    '''
    Compte le nombre de fois qu'un verrou passe par le chiffre 0 étant donné une suite d'instruction
    '''

    # fonctions auxiliaires
    def R(n: int, delta: int):
        '''
        incrémente n de delta modulo 100
        retourne le tuple composé du résultat et du nombre passage par zéro
        '''
        zeros = 0
        while delta > 99: # pour chaque dépassement de 99
            delta -= 100
            zeros += 1

        if n + delta > 99: # dernier dépassement
            n = (n + delta) % 100
            zeros += 1
        else:
            n += delta # sinon, pas de dépassement

        return n, zeros

    def L(n: int, delta: int):
        '''
        décrémente n de delta modulo 100
        retourne le tuple composé du résultat et du nombre passage par zéro
        '''
        zeros = 0
        if n == 0: # si déjà à zéro, le passage a déjà été compté
            zeros -= 1
        while delta > 99: # pour chaque passage par 0
            delta -= 100
            zeros += 1

        if delta >= n: # dépassement supplémentaire
            n = (n - delta) % 100
            zeros += 1
        else: # sinon, pas de dépassement
            n -= delta
            
        return n, zeros

    # corps de la fonction
    instructions = parse(fileName, liste=True)
    
    res = 0
    n = 50
    for instr in instructions:
        zeros = 0
        if instr != "" and instr[0] == 'R': # décalage vers la droite
            n, zeros = R(n, int(instr[1:]))
        elif instr != "" and instr[0] == 'L': # décalage vers la gauche
            n, zeros = L(n, int(instr[1:]))
        else:
            continue # instruction invalide
        res += zeros # incrémente par le nombre de passage par zéro
    
    return res
