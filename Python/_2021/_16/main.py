dico = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111",
}

def extract(n: int, L):
    txt = L[:n]
    return txt, L[n:]

def extract_sub(txt):
    version, txt = extract(3, txt)
    ID, txt = extract(3, txt)

    if ID == "100":
        total_sub = ""
        sub, txt = extract(5, txt)
        total_sub += sub
        while sub[0] == "1":
            sub, txt = extract(5, txt)
            total_sub += sub
        return version + ID + total_sub, txt
    
    I, txt = extract(1, txt)
    if I == "0":
        length, txt = extract(15, txt)
        sub, txt = extract(bin_to_int(length), txt)
        return version + ID + I + length + sub, txt
    else:
        sub_nb, txt = extract(11, txt)
        nb = 0
        sub = ""
        while nb != bin_to_int(sub_nb):
            ssub, txt = extract_sub(txt)
            sub += ssub
            nb += 1
        return version + ID + I + sub_nb + sub, txt

def bin_to_int(txt) -> int:
    if txt == '':
        return 0
    return int(txt[-1]) + 2*bin_to_int(txt[:-1])

## result1

def result1(L, hexa=True):
    txt = ""
    if hexa:
        for x in L[0][0]:
            txt += dico[x]
    else:
        txt = L
    
    version, txt = extract(3, txt)
    version = bin_to_int(version)

    ID, txt = extract(3, txt)
    ID = bin_to_int(ID)

    if ID == 4:
        # print(version, ID, txt)
        return version
    
    I, txt = extract(1, txt)
    
    if I == "0":
        length, txt = extract(15, txt)
        length = bin_to_int(length)

        # print(version, ID, I, length, txt)

        sub, txt = extract(length, txt)

        s = 0
        while sub:
            ssub, sub = extract_sub(sub)
            s += result1(ssub, False)
        
        return s + version
    
    else:
        sub_nb, txt = extract(11, txt)
        sub_nb = bin_to_int(sub_nb)

        # print(version, ID, I, sub_nb, txt)

        nb = 0
        s = 0
        while nb != sub_nb:
            ssub, txt = extract_sub(txt)
            s += result1(ssub, False)
            nb += 1
        
        return s + version
    
## result2

def result2(L, hexa=True):
    txt = ""
    if hexa:
        for x in L[0][0]:
            txt += dico[x]
    else:
        txt = L
    
    version, txt = extract(3, txt)
    version = bin_to_int(version)

    ID, txt = extract(3, txt)
    ID = bin_to_int(ID)

    if ID == 4:
        s = 0
        sub, txt = extract(5, txt)
        s += bin_to_int(sub[1:])
        while sub[0] == "1":
            sub, txt = extract(5, txt)
            s += bin_to_int(sub[1:])
        
        return s
    
    I, txt = extract(1, txt)

    l_int = []
    
    if I == "0":
        length, txt = extract(15, txt)
        length = bin_to_int(length)

        sub, txt = extract(length, txt)

        while sub:
            ssub, sub = extract_sub(sub)
            l_int.append(result2(ssub, False))
    
    else:
        sub_nb, txt = extract(11, txt)
        sub_nb = bin_to_int(sub_nb)

        nb = 0
        while nb != sub_nb:
            ssub, txt = extract_sub(txt)
            l_int.append(result2(ssub, False))
            nb += 1
        
    match ID:
        case 0:
            return sum(l_int)
        case 1:
            p = 1
            for x in l_int:
                p *= x
            return p
        case 2:
            return min(l_int)
        case 3:
            return max(l_int)
        case 5:
            return int(l_int[0] >= l_int[1])
        case 6:
            return int(l_int[0] <= l_int[1])
        case 7:
            return int(l_int[0] == l_int[1])
        case _:
            raise Exception("wtf")