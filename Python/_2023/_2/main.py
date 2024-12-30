

## result1

def result1(L):
    s = 0
    for l in L:
        possible = True
        for i in range(len(l)):
            if "red" in l[i]:
                if int(l[i-1]) > 12:
                    possible = False
            elif "green" in l[i]:
                if int(l[i-1]) > 13:
                    possible = False
            elif "blue" in l[i]:
                if int(l[i-1]) > 14:
                    possible = False
        if possible:
            s += int(l[1][:-1])
    return s

## restult2


def result2(L):
    s = 0
    for l in L:
        possible = True
        f_r = 0
        f_g = 0
        f_b = 0
        for i in range(len(l)):
            if "red" in l[i]:
                f_r = max(int(l[i-1]), f_r)
            elif "green" in l[i]:
                f_g = max(int(l[i-1]), f_g)
            elif "blue" in l[i]:
                f_b = max(int(l[i-1]), f_b)
        s += f_r*f_g*f_b
    return s
