class Board:
    def __init__(self, L) -> None:
        self.mirrors = L
        self.energies = [[(0, 0)]*len(L[0]) for _ in range(len(L))]
    
    def next(self, stack:list[tuple[int, int, int, int]]):
        while stack:
            i, j, di, dj = stack.pop()
            if i < 0 or i >= len(self.mirrors) or j < 0 or j >= len(self.mirrors[0]):
                continue
            if self.mirrors[i][j] == ".":
                if self.energies[i][j][0] == 1 and di in {1, -1}:
                    continue
                if self.energies[i][j][1] == 1 and dj in {1, -1}:
                    continue
            match self.mirrors[i][j]:
                case ".":
                    if di in {1, -1}:
                        self.energies[i][j] = (1, self.energies[i][j][1])
                        stack.append((i+di, j, di, dj))
                    else:
                        self.energies[i][j] = (self.energies[i][j][0], 1)
                        stack.append((i, j+dj, di, dj))
                case "/":
                    if di == 1 or dj == 1:
                        self.energies[i][j] = (1, self.energies[i][j][1])
                        stack.append((i-dj, j-di, -dj, -di))
                    else:
                        self.energies[i][j] = (self.energies[i][j][0], 1)
                        stack.append((i-dj, j-di, -dj, -di))
                case "\\":
                    if di == 1 or dj == -1:
                        self.energies[i][j] = (1, self.energies[i][j][1])
                        stack.append((i+dj, j+di, dj, di))
                    else:
                        self.energies[i][j] = (self.energies[i][j][0], 1)
                        stack.append((i+dj, j+di, dj, di))
                case "|":
                    if di in {1, -1}:
                        self.energies[i][j] = (1, 0)
                        stack.append((i+di, j, di, dj))
                    else:
                        self.energies[i][j] = (1, 0)
                        stack.append((i-1, j, -1, 0))
                        stack.append((i+1, j, 1, 0))
                case "-":
                    if dj in {1, -1}:
                        self.energies[i][j] = (0, 1)
                        stack.append((i, j+dj, di, dj))
                    else:
                        self.energies[i][j] = (0, 1)
                        stack += [(i, j+1, 0, 1)]
                        stack.append((i, j-1, 0, -1))
    
    def get_energies(self):
        ener = 0
        for l in self.energies:
            ener += len([c for c in l if c != (0, 0)])
        return ener
    
    def __str__(self) -> str:
        txt = ""
        for i in range(len(self.mirrors)):
            for j in range(len(self.mirrors[0])):
                if self.energies[i][j] == (0, 0):
                    txt += f"."
                else:
                    txt += f"#"
            txt += "\n"
        return txt

## result1

def result1(L):
    L = [l[0] for l in L]
    board = Board(L)
    board.next([(0, 0, 0, 1)])
    # print(board)
    return board.get_energies()
    
## restult2

def result2(L):
    L = [l[0] for l in L]
    maximum = 0
    for i in range(len(L)):
        b = Board(L)
        b.next([(i, 0, 0, 1)])
        maximum = max(maximum, b.get_energies())

        b = Board(L)
        b.next([(i, len(L[0])-1, 0, 1)])
        maximum = max(maximum, b.get_energies())

    for j in range(len(L[0])):
        b = Board(L)
        b.next([(0, j, 1, 0)])
        maximum = max(maximum, b.get_energies())

        b = Board(L)
        b.next([(len(L)-1, j, -1, 0)])
        maximum = max(maximum, b.get_energies())
    
    return maximum