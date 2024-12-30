seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

L_dico = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location,
]

def follow(L_dico, n):
    for dico in L_dico:
        found = False
        for l in dico:
            if l[0] <= n and n < l[0]+l[2] and not found:
                n += (l[1]-l[0])
                found = True
    return n

## result1

def result1(L):
    dico = -1
    for l in L[1:]:
        if l[-1] == "map:":
            dico += 1
        else:
            L_dico[dico].append((int(l[1]), int(l[0]), int(l[2])))
    l = [int(x) for x in L[0][1:]]
    l_loc = [follow(L_dico, x) for x in l]
    return min(l_loc)

## restult2

def follow_range(dico, c):
    n0, n1 = c
    for l in dico:
        if l[0] <= n0 and n1 < l[0]+l[2]:
            return [(n0+l[1]-l[0], n1+l[1]-l[0])]
        elif l[0] <= n0 and n0 < l[0]+l[2] and n1 >= l[0]+l[2]:
            return [(n0+l[1]-l[0], l[1]+l[2]-1)]+follow_range(dico, (l[0]+l[2], n1))
        elif n0 < l[0] and l[0] <= n1 and n1 < l[0]+l[2]:
            return [(l[1], n1+l[1]-l[0])]+follow_range(dico, (n0, l[0]-1))
        elif n0 < l[0] and l[0]+l[2] <= n1:
            return follow_range(dico, (n0, l[0]-1))+[(l[1], l[1]+l[2]-1)]+follow_range(dico, (l[0]+l[2], n1))
    return [(n0, n1)]

def result2(L):
    dico = -1
    for l in L[1:]:
        if l[-1] == "map:":
            dico += 1
        else:
            L_dico[dico].append((int(l[1]), int(l[0]), int(l[2])))
    l_ = L[0][1:]
    l_seed = []
    i = 0
    while i < len(l_):
        l_seed += [(int(l_[i]), int(l_[i])+int(l_[i+1])-1)]
        i += 2
    for dico in L_dico:
        n_l_seed = []
        for c in l_seed:
            n_l_seed += follow_range(dico, c)
        l_seed = n_l_seed
    return min(c[0] for c in l_seed)