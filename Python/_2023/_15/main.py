def hash(txt):
    value = 0
    for c in txt:
        value += ord(c)
        value *= 17
        value %= 256
    return value

## result1

def result1(L):
    L = L[0]
    return sum([hash(x) for x in L])
    
## restult2

def replace_lens(box, label, lens):
    for i in range(len(box)):
        if box[i][0] == label:
            box[i] = (label, lens)
            return box
    box.append((label, lens))
    return box

def result2(L):
    L = L[0]
    boxes = [[] for _ in range(256)]
    for instr in L:
        label = ""
        operator = ""
        lens = -1
        if instr[-1] == "-":
            operator = "-"
            label = instr[:-1]
        else:
            operator = "="
            label = instr[:-2]
            lens = int(instr[-1])

        if operator == "=":
            boxe_index = hash(label)
            boxes[boxe_index] = replace_lens(boxes[boxe_index], label, lens)
        else:
            boxe_index = hash(label)
            boxes[boxe_index] = [c for c in boxes[boxe_index] if c[0] != label]
    
    score = 0
    for i_boxe in range(len(boxes)):
        for i_label in range(len(boxes[i_boxe])):
            score += (1+i_boxe)*(1+i_label)*boxes[i_boxe][i_label][1]
    
    return score