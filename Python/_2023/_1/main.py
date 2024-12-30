

## result1

def result1(L):
    s = 0
    for x in [x[0] for x in L if len(x[0])!= 0]:
        l = []
        for letter in x:
            if letter != "" and letter in "0123456789":
                l.append(letter)
        s += int(l[0]+l[-1])
    return s

## restult2

def is_in(word, list) -> str:
    if word == "":
        return ""
    if word in list:
        return word
    return is_in(word[1:], list)

def get_index(word, l1, l2):
    for i in range(len(l1)):
        if word == l1[i]:
            return i+1
    for i in range(len(l2)):
        if word == l2[i]:
            return i+1
    raise Exception("Not found")

def result2(L):
    L = [x[0] for x in L]

    list_digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    s = 0
    total = 0
    for x in L:
        line = x.strip()
        first = None
        last = None

        curr_string = ""

        for c in line:
            if c.isdigit():
                if first is None:
                    first = int(c)
                last = int(c)
                curr_string = ""
                continue

            curr_string += c
            for itx, num in enumerate(list_number):
                if num in curr_string:
                    if first is None:
                        first = itx + 1
                    last = itx + 1
                    curr_string = curr_string[-1]
                    break

        val = first * 10 + last
        total += val
    return total