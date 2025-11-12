from parse import parse
import re # regular expression

def part1(fileName: str):
    """
    Exécute les instructions du fichiers qui sont bien parsées et renvoie le résultat de ces instructions
    """
    # parse le fichier
    data = parse(fileName, texte=True)

    res = 0
    # récupère tous les "mul()" bien formés
    p = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
    for (a, b) in [re.findall(r'\d+', mul) for mul in p]:
        res += int(a) * int(b) # multiplie les nombres en question
    return res

def part2(fileName: str):
    """
    Exécute les instructions du fichiers qui sont bien parsées et renvoie le résultat de ces instructions. Cela inclue "mul", "do" et "don't"
    """
    # parse le fichier
    data = parse(fileName, texte=True)

    res = 0
    # récupère tous les "mul()" bien formés
    p = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', data)
    doIt = True
    for m in p:
        if m == "do()": # active la multiplication
            doIt = True
        elif m == "don't()": # désactive la multiplication
            doIt = False
        elif doIt: # n'effectue la multiplication ssi active
            (a, b) = re.findall(r'\d+', m)
            res += int(a) * int(b)
    return res
