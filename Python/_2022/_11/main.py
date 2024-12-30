from tqdm import tqdm

class Monkey:
    def __init__(self, n: int, items: list[int], operation: list[str], test: int, cond: tuple[int, int], divide: bool=True) -> None:
        self.n = n
        self.items = items
        self.test = test
        self.operation = operation # value1, value2, operator
        self.cond = cond # True, False

        self.nb_inspection = 0
        self.divide = divide

    def inspect(self) -> None:
        for i in range(len(self.items)):
            x = self.items[i]

            values = [0, 0]
            for j in range(2):
                if self.operation[j] == "old":
                    values[j] = x
                else:
                    values[j] = int(self.operation[j])
            
            match self.operation[2]:
                case "+":
                    self.items[i] = values[0]+values[1]
                case "*":
                    self.items[i] = values[0]*values[1]
                case _:
                    raise Exception("WTF")
        
        if self.divide:
            self.items = [int(x/3) for x in self.items]
        
    def throw(self):
        self.inspect()
        self.nb_inspection += len(self.items)
        L = []
        for x in self.items:
            if not x%self.test:
                L.append((self.cond[0], x))
            else:
                L.append((self.cond[1], x))
        self.items = []
        return L

def round(list_of_monkeys: list[Monkey]):
    for monkey in list_of_monkeys:
        l = monkey.throw()
        for m, v in l:
            list_of_monkeys[m].items.append(v)

## result1

def result1(L):
    monkeys: list[list] = []
    for l in L:
        if l[0] == "Monkey":
            monkeys.append([])
        monkeys[-1].append(l)
        
    list_of_monkeys: list[Monkey] = []
    for l in monkeys:
        list_of_monkeys.append(
            Monkey(
                int(l[0][-1]),
                [int(x) for x in l[1][2:]],
                [l[2][-3], l[2][-1], l[2][-2]],
                int(l[3][-1]),
                (int(l[4][-1]), int(l[5][-1]))
            )
        )

    for i in range(20):
        round(list_of_monkeys)
    
    m1, m2 = 0, 0
    for monkey in list_of_monkeys:
        if monkey.nb_inspection > m2:
            m1 = m2
            m2 = monkey.nb_inspection
        elif monkey.nb_inspection > m1:
            m1 = monkey.nb_inspection
    
    return m1 * m2
    
## result2

def result2(L):
    monkeys: list[list] = []
    for l in L:
        if l[0] == "Monkey":
            monkeys.append([])
        monkeys[-1].append(l)
        
    list_of_monkeys: list[Monkey] = []
    for l in monkeys:
        list_of_monkeys.append(
            Monkey(
                int(l[0][-1]),
                [int(x) for x in l[1][2:]],
                [l[2][-3], l[2][-1], l[2][-2]],
                int(l[3][-1]),
                (int(l[4][-1]), int(l[5][-1])),
                divide=False
            )
        )

    for i in tqdm(range(10000)):
        round(list_of_monkeys)
    
    m1, m2 = 0, 0
    for monkey in list_of_monkeys:
        if monkey.nb_inspection > m2:
            m1 = m2
            m2 = monkey.nb_inspection
        elif monkey.nb_inspection > m1:
            m1 = monkey.nb_inspection
    
    return m1 * m2