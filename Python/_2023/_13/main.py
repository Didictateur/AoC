class Grid:
    def __init__(self) -> None:
        self.grid: list[str] = []

    def add_row(self, row):
        self.grid.append(list(row))

    def has_row_sym(self):
        L_sym = all_sym(self.grid[0])
        i = 1
        while L_sym and i < len(self.grid):
            L_sym = intersect(L_sym, all_sym(self.grid[i]))
            i += 1
        if L_sym:
            return L_sym[0]
        return -1
    
    def has_col_sym(self):
        L_sym = all_sym([row[0] for row in self.grid])
        i = 1
        while L_sym and i < len(self.grid[0]):
            L_sym = intersect(L_sym, all_sym([row[i] for row in self.grid]))
            i += 1
        if L_sym:
            assert len(L_sym) == 1
            return L_sym[0]
        return -1
    
    def find_value(self):
        r = self.has_row_sym()
        if r != -1:
            assert r != 0
            return (r, "column")
        c = self.has_col_sym()
        assert c != -1 and c != 0
        return (c, "row")

def has_sym(l, i):
    l1 = l[:i]
    l2 = l[i:]
    l1.reverse()
    if len(l1) > len(l2):
        return include(l2, l1)
    return include(l1, l2)

def include(l1, l2):
    if len(l1) > len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True

def intersect(l1, l2):
    return [x for x in l1 if x in l2]

def all_sym(l):
    L_sym = []
    for i in range(1, len(l)):
        if has_sym(l, i):
            L_sym.append(i)
    return L_sym

## result1

def result1(L):
    L = [l[0] for l in L]
    L_grid = [Grid()]
    for l in L:
        if "X" in l:
            L_grid.append(Grid())
        else:
            L_grid[-1].add_row(l)
    
    R = 0
    C = 0

    for g in L_grid:
        v, t = g.find_value()
        if t == "row":
            R += v
        else:
            C += v
    
    return C+100*R
    
## restult2

def result2(L):
    pass