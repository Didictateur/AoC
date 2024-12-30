from tqdm import tqdm
from math import *
from Pyvyctor import Vector2d

def draw(ground):
    for l in ground:
        print("".join([["#", "x", "."][c] for c in l]))

def interpret(l):
    hexa = "0123456789abcdef"
    dec = 0
    for x in l[2][2:-2]:
        dec *= 16
        dec += hexa.index(x)
    return dec, ["R", "D", "L", "U"][int(l[2][-2])]

class Planimeter:
    def __init__(self, center, rotation, pointe) -> None:
        assert abs((rotation-center).norm() - (rotation-pointe).norm()) < 10**(-3)
        self.center = center
        self.rotation = rotation
        self.pointe = pointe
        self.value = 0
        self.len = (rotation-pointe).norm()
    
    def __add__(self, dp: tuple[int, int]) -> None:
        self.pointe += Vector2d(*dp)
        tosym = (self.pointe-self.center)/2
        length = tosym.norm()
        ortholength = sqrt(self.len**2-length**2)
        orthovect = Vector2d(-tosym.y, tosym.x)/length*ortholength
        pa = self.center+tosym+orthovect
        pb = self.center+tosym-orthovect
        if (self.rotation-pa).norm() < (self.rotation-pb).norm():
            self.rotation = pa
        else:
            self.rotation = pb
        self.value += ((self.pointe-self.rotation)/self.len).dot(Vector2d(*dp))
    
    def get_valuation(self) -> int:
        return self.value*self.len

## result1

def result1(L):
    ground = [[0]]
    x, y = 0, 0
    for dir, step, color in L:
        step = int(step)
        # draw(ground)
        # input()
        match dir:
            case "L":
                for i in range(step):
                    i, j = x-1, y
                    while i >= 0 and ground[i][j] != 0:
                        ground[i][j] = 1
                        i -= 1
                    i, j = x+1, y
                    while i < len(ground) and ground[i][j] != 0:
                        ground[i][j] = -1
                        i += 1

                    y -= 1
                    if y < 0:
                        ground = [[-1]+l for l in ground]
                        y += 1
                    ground[x][y] = 0

                    i, j = x-1, y
                    while i >= 0 and ground[i][j] != 0:
                        ground[i][j] = 1
                        i -= 1
                    i, j = x+1, y
                    while i < len(ground) and ground[i][j] != 0:
                        ground[i][j] = -1
                        i += 1

            case "R":
                for i in range(step):
                    i, j = x-1, y
                    while i >= 0 and ground[i][j] != 0:
                        ground[i][j] = -1
                        i -= 1
                    i, j = x+1, y
                    while i < len(ground) and ground[i][j] != 0:
                        ground[i][j] = 1
                        i += 1

                    y += 1
                    if y >= len(ground[0]):
                        ground = [l+[-1] for l in ground]
                    ground[x][y] = 0

                    i, j = x-1, y
                    while i >= 0 and ground[i][j] != 0:
                        ground[i][j] = -1
                        i -= 1
                    i, j = x+1, y
                    while i < len(ground) and ground[i][j] != 0:
                        ground[i][j] = 1
                        i += 1

            case "U":
                for i in range(step):
                    i, j = x, y-1
                    while j >= 0 and ground[i][j] != 0:
                        ground[i][j] = -1
                        j -= 1
                    i, j = x, y+1
                    while j < len(ground[0]) and ground[i][j] != 0:
                        ground[i][j] = 1
                        j += 1

                    x -= 1
                    if x < 0:
                        ground.insert(0, [-1 for _ in range(len(ground[0]))])
                        x += 1
                    ground[x][y] = 0

                    i, j = x, y-1
                    while j >= 0 and ground[i][j] != 0:
                        ground[i][j] = -1
                        j -= 1
                    i, j = x, y+1
                    while j < len(ground[0]) and ground[i][j] != 0:
                        ground[i][j] = 1
                        j += 1

            case "D":
                for i in range(step):
                    i, j = x, y-1
                    while j >= 0 and ground[i][j] != 0:
                        ground[i][j] = 1
                        j -= 1
                    i, j = x, y+1
                    while j < len(ground[0]) and ground[i][j] != 0:
                        ground[i][j] = -1
                        j += 1

                    x += 1
                    if x >= len(ground):
                        ground.append([-1 for _ in range(len(ground[0]))])
                    ground[x][y] = 0

                    i, j = x, y-1
                    while j >= 0 and ground[i][j] != 0:
                        ground[i][j] = 1
                        j -= 1
                    i, j = x, y+1
                    while j < len(ground[0]) and ground[i][j] != 0:
                        ground[i][j] = -1
                        j += 1

    # draw(ground)
    
    nb = [0, 0, 0]
    for i in range(len(ground)):
        for j in range(len(ground[0])):
            nb[ground[i][j]] += 1

    return nb[0]+nb[1]
    
## restult2

def result2(L):
    L = [interpret(l) for l in L]

    plan = Planimeter(Vector2d(-10000000, -10000000), Vector2d(0, -10000000), Vector2d(0, 0))

    for l in L:
        dx = 0
        dy = 0
        match l[1]:
            case "R":
                dx = 1
            case "L":
                dx = -1
            case "U":
                dy = -1
            case "D":
                dy = 1
        for i in range(l[0]):
            plan + (dx, dy)

    return plan.get_valuation()