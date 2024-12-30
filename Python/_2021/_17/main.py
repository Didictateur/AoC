def y_in(ymin: int, ymax: int, vy: int):
    y = 0
    while vy > 0:
        if ymin <= y and y <= ymax:
            return True
        y += vy
        vy -= 1
    while y >= ymin:
        if ymin <= y and y <= ymax:
            return True
        y += vy
        vy -= 1
    return False

def max_y(vy):
    y = 0
    while vy >0:
        y += vy
        vy -= 1
    return y

def is_in(dx, dy, xmin, xmax, ymin, ymax) -> bool:
    x, y = 0, 0

    while x <= xmax and y >= ymin:
        if x >= xmin and y <= ymax:
            return True
        
        x += dx
        y += dy

        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        else:
            if x < xmin:
                return False
        dy -= 1
    
    return False

## result1

def result1(L):
    xmin, xmax = L[0][0], L[0][1]
    ymin, ymax = L[1][0], L[1][1]

    dy = 0
    for vy in range(max(abs(ymin), abs(ymax))+3):
        if y_in(ymin, ymax, vy):
            dy = vy

    return max_y(dy)
    
## result2

def result2(L):
    xmin, xmax = L[0][0], L[0][1]
    ymin, ymax = L[1][0], L[1][1]

    s = 0
    for dx in range(xmax+1):
        for dy in range(ymin, -ymin+1):
            if is_in(dx, dy, xmin, xmax, ymin, ymax):
                s += 1

    return s