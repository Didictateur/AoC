## result1

def result1(L):
    X = 1
    ticks = 0
    s = 0
    for l in L:
        if l[0] == "noop":
            ticks += 1
            if ticks >= 20 and (ticks-20)%40 == 0:
                s += ticks * X
        elif l[0] == "addx":
            ticks += 1
            if ticks >= 20 and (ticks-20)%40 == 0:
                s += ticks * X
            ticks += 1
            if ticks >= 20 and (ticks-20)%40 == 0:
                s += ticks * X
            X += int(l[1])
    return s
    
## result2

def result2(L):
    X = 1
    ticks = 0
    s = 0
    draw = []
    for l in L:
        if l[0] == "noop":
            ticks += 1
            if (len(draw)+1)%40 in {X, X+1, X+2}:
                draw.append("#")
            else:
                draw.append(".")
            if ticks >= 20 and (ticks-20)%40 == 0:
                s += ticks * X
        elif l[0] == "addx":
            ticks += 1
            if (len(draw)+1)%40  in {X, X+1, X+2}:
                draw.append("#")
            else:
                draw.append(".")
            if ticks >= 20 and (ticks-20)%40 == 0:
                s += ticks * X
            ticks += 1
            if (len(draw)+1)%40  in {X, X+1, X+2}:
                draw.append("#")
            else:
                draw.append(".")
            if ticks >= 20 and (ticks-20)%40 == 0:
                s += ticks * X
            X += int(l[1])

    d = ""
    for k in range(len(draw)//40):
        for i in range(40):
            d += draw[40*k+i]
        d += '\n'
    return d