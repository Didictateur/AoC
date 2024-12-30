class Platfomr:
    def __init__(self, grid) -> None:
        self.grid = []
        for l in grid:
            self.grid.append([])
            for c in l:
                if c == ".":
                    self.grid[-1].append(0)
                elif c == "#":
                    self.grid[-1].append(-1)
                else:
                    self.grid[-1].append(1)
        
    def tilting_north(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    x, y = i, j
                    while x > 0 and self.grid[x-1][y] == 0:
                        self.grid[x][y], self.grid[x-1][y] = self.grid[x-1][y], self.grid[x][y]
                        x -= 1
    
    def tilting_south(self):
        for i in range(len(self.grid))[::-1]:
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    x, y = i, j
                    while x < len(self.grid)-1 and self.grid[x+1][y] == 0 :
                        self.grid[x][y], self.grid[x+1][y] = self.grid[x+1][y], self.grid[x][y]
                        x += 1
    
    def tilting_east(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0]))[::-1]:
                if self.grid[i][j] == 1:
                    x, y = i, j
                    while y < len(self.grid[0])-1 and self.grid[x][y+1] == 0:
                        self.grid[x][y], self.grid[x][y+1] = self.grid[x][y+1], self.grid[x][y]
                        y += 1
    
    def tilting_west(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    x, y = i, j
                    while y > 0 and self.grid[x][y-1] == 0:
                        self.grid[x][y], self.grid[x][y-1] = self.grid[x][y-1], self.grid[x][y]
                        y -= 1
    
    def north_load(self):
        load = 0
        n = len(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    load += n - i
        return load

    def cycle(self):
        self.tilting_north()
        self.tilting_west()
        self.tilting_south()
        self.tilting_east()
    
    def copy(self):
        g = Platfomr([])
        g.grid = []
        for l in self.grid:
            g.grid.append(l.copy())
        return g
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Platfomr):
            return self.grid == __value.grid
        return False
    
    def __str__(self) -> str:
        return "\n".join(["".join([".O#"[c] for c in l]) for l in self.grid])

## result1

def result1(L):
    L = [l[0] for l in L]
    plat = Platfomr(L)
    plat.tilting_north()
    return plat.north_load()
    
## restult2

def result2(L):
    L = [l[0] for l in L]
    plat = Platfomr(L)
    L_plat = [plat.copy()]
    for _ in range(1000000000):
        plat.cycle()
        # input()
        # print(plat)
        if plat in L_plat:
            break
        L_plat.append(plat.copy())

    index = -1
    for i in range(len(L_plat)):
        if L_plat[i] == plat:
            index = i
            break
    # index += 1
    # print(index)
    L_path = L_plat[:index]
    L_loop = L_plat[index:]

    # print(L_loop[0])
    # c = L_loop[-1]
    # print()
    # print(c)
    # c.cycle()
    # print()
    # print(c)
    # assert L_loop[0] == c

    nbcycle = 1000000000
    L_cycle = L_path
    while len(L_cycle) < nbcycle:
        L_cycle += L_loop

    return L_cycle[nbcycle].north_load()