class FlipFlop:
    def __init__(self, name: str, destinations: list[str], status: bool=False,) -> None:
        self.name = name
        self.status = status
        self.destinations = destinations
    
    def recieve(self, sender: str, pulse: bool):
        if pulse:
            return []
        self.status = not self.status
        return [(self.name, self.status, dest) for dest in self.destinations]

class Conjonctions:
    def __init__(self, name: str, destinations: list[str], dico) -> None:
        self.name = name
        self.destinations = destinations
        self.dico = dico
    
    def recieve(self, sender, pulse):
        for x in [x for x in self.dico if type(x)==FlipFlop]:
            if self.name in self.dico[x].destinations and not self.dico[x].status:
                return [(self.name, True, destin) for destin in self.destinations]
        return [(self.name, False, destin) for destin in self.destinations]

class Broadcaster:
    def __init__(self, name: str, destinations: list[str]) -> None:
        self.name = name
        self.destinations = destinations

    def recieve(self, sender: str, pulse: bool):
        return [(self.name, pulse, dest) for dest in self.destinations]

## result1

def result1(L):
    dico = {}
    for l in L:
        if l[0][0] == "%":
            name = l[0][1:]
            destinations = []
            for x in l[2:]:
                if x[-1] == ',':
                    x = x[:-1]
                destinations.append(x)
            dico[name] = FlipFlop(name, destinations)
        elif l[0][0] == "&":
            name = l[0][1:]
            destinations = []
            for x in l[2:]:
                if x[-1] == ',':
                    x = x[:-1]
                destinations.append(x)
            dico[name] = Conjonctions(name, destinations, dico)
        elif l[0] == "broadcaster":
            name = l[0]
            destinations = []
            for x in l[2:]:
                if x[-1] == ',':
                    x = x[:-1]
                destinations.append(x)
            dico[name] = Broadcaster(name, destinations)
        else:
            raise Exception("Invalid input")

    count_pulse = [0, 0]
    old_dico = dico.copy()
    can_copy = False

    def equal_dic(d1, d2) -> bool:
        for x in d1:
            if type(d1[x]) != type(d2[x]):
                return False
            if type(d1[x]) == FlipFlop:
                if d1[x].status != d2[x].status:
                    return False
        return True

    for i in range(1000):
        if can_copy:
            count_pulse[0] += count_pulse[0]
            count_pulse[1] += count_pulse[1]
        else:
            l_count = [0, 0]
            L_pulse = [("", False, "broadcaster")]
            while L_pulse:
                sender, pulse, dest = L_pulse[0]
                print(i, sender, pulse, dest)
                l_count[int(pulse)] += 1
                if dest in dico:
                    L_pulse = L_pulse[1:] + dico[dest].recieve(sender, pulse)
                else:
                    L_pulse = L_pulse[1:]
            if equal_dic(old_dico, dico):
                can_copy = True
                print("copy !")
            count_pulse[0] += l_count[0]
            count_pulse[1] += l_count[1]

    return count_pulse, count_pulse[0]*count_pulse[1]
    
## restult2

def result2(L):
    pass