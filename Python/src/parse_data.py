def parse(y: int, d: int, integer: bool=False, test: bool=False):
    filename = "data.txt"
    if test:
        filename = "test.txt"
    with open(f"/home/jupiter/Bureau/AoC/Python/_{y}/_{d}/{filename}", "r") as f:
        L = []
        for line in [line.split() for line in f.readlines() if line.split() != []]:
            if integer:
                L.append([int(x) for x in line])
            else:
                L.append(line)
    return L