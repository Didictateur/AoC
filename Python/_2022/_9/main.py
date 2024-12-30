class Rope:
    def __init__(self, n: int):
        self.x = 0
        self.y = 0
        self.visited = [(0, 0)]

        self.tail = None
        if n != 0:
            self.tail = Rope(n-1)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if not (self.x, self.y) in self.visited:
            self.visited.append((self.x, self.y))
        if self.tail is not None:
            if abs(self.x-self.tail.x) > 1 or abs(self.y-self.tail.y) > 1:
                match (self.x-self.tail.x, self.y-self.tail.y):
                    case (0, 2):
                        self.tail.move(0, 1)
                    case (1, 2) | (2, 2) | (2, 1):
                        self.tail.move(1, 1)
                    case (2, 0):
                        self.tail.move(1, 0)
                    case (2, -1) | (2, -2) | (1, -2):
                        self.tail.move(1, -1)
                    case (0, -2):
                        self.tail.move(0, -1)
                    case (-1, -2) | (-2, -2) | (-2, -1):
                        self.tail.move(-1, -1)
                    case (-2, 0):
                        self.tail.move(-1, 0)
                    case (-2, 1) | (-2, 2) | (-1, 2):
                        self.tail.move(-1, 1)
                    case _:
                        raise Exception("WTF !?")
    
    def interprete_move(self, dir: str, step: int) -> None:
        match dir:
            case "R":
                for i in range(step):
                    self.move(1, 0)
            case "U":
                for i in range(step):
                    self.move(0, 1)
            case "D":
                for i in range(step):
                    self.move(0, -1)
            case "L":
                for i in range(step):
                    self.move(-1, 0)
    
    def tail_visited(self):
        if self.tail is None:
            return self.visited
        return self.tail.tail_visited()

## result1

def result1(L):
    r = Rope(1)

    for l in L:
        r.interprete_move(l[0], int(l[1]))
    
    return len(r.tail.visited)
    
## result2

def result2(L):
    r = Rope(9)

    for l in L:
        r.interprete_move(l[0], int(l[1]))
    
    return len(r.tail_visited())