from sys import argv, modules
from importlib.util import spec_from_file_location, module_from_spec

# vérifie le nombre d'argument
if len(argv) != 3:
    raise Exception("Format attendu: 'python main.py <année> <jour>'")

# vérifie la validité des arguments
try:
    annee = int(argv[1])
    jour = int(argv[2])
except:
    raise Exception("Le format du jour et/ou de l'année ne sont pas valides")

# exécution du programme correspondant
try:
    dirPath = f"{annee}/{jour}" # chemin du dossier
    mainPath = dirPath + "/main.py" # chemin du main
    testPath = dirPath + "/test.txt" # chemin vers les données tests
    dataPath = dirPath + "/data.txt" # chemin vers les données

    # charger le code du fichier choisit
    spec = spec_from_file_location("code", mainPath)
    module = module_from_spec(spec)
    modules["code"] = module
    spec.loader.exec_module(module)

    # exécuter la fonction
    res1_t = module.part1(testPath)
    res1 = module.part1(dataPath)
    res2_t = module.part2(testPath)
    res2 = module.part2(dataPath)

    # Affichage des résultats
    print("Part 1:")
    print(f"Test : {res1_t}")
    print(f"Data : {res1}\n")
    print("Part 2:")
    print(f"Test : {res2_t}")
    print(f"Data : {res2}\n")

except Exception as e:
    print(e)
    exit(1)


