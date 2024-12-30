class Card:
    def __init__(self, label:str, joker = False) -> None:
        self.value = -1
        self.joker = joker
        dico = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        if joker:
            dico = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
        for i in range(len(dico)):
            if label == dico[i]:
                self.value = i
        if self.value == -1:
            raise Exception(f"Uknown label {label}")
        
    def __eq__(self, __value):
        return self.value == __value.value
    
    def __lt__(self, __value):
        return self.value < __value.value
    
    def __gt__(self, __value):
        return self.value > __value.value
    
    def __lte_(self, __value):
        return self.value <= __value.value
    
    def __ge__(self, __value):
        return self.value >= __value.value
    
class Hand:
    def __init__(self, hand: str, bid: int, joker = False) -> None:
        self.cards = [Card(e, joker) for e in hand]
        assert len(self.cards) == 5
        self.rank = -1
        self.bid = bid
        self.joker = joker

        L = [0]*13

        if not self.joker:
            for card in self.cards:
                L[card.value] += 1
            
            if 5 in L:
                self.rank = 6
            elif 4 in L:
                self.rank = 5
            elif 3 in L and 2 in L:
                self.rank = 4
            elif 3 in L:
                self.rank = 3
            elif len([x for x in L if x == 2]) == 2:
                self.rank = 2
            elif 2 in L:
                self.rank = 1
            elif 1 in L:
                self.rank = 0
            else:
                raise Exception("wtf")
        else:
            for card in self.cards:
                L[card.value] += 1
            m = 0
            index = 0
            for i in range(len(L[1:])):
                if L[i+1] >= m:
                    index = i+1
                    m = L[i+1]
            L[index] += L[0]
            L[0] = 0
            
            if 5 in L:
                self.rank = 6
            elif 4 in L:
                self.rank = 5
            elif 3 in L and 2 in L:
                self.rank = 4
            elif 3 in L:
                self.rank = 3
            elif len([x for x in L if x == 2]) == 2:
                self.rank = 2
            elif 2 in L:
                self.rank = 1
            elif 1 in L:
                self.rank = 0
            else:
                raise Exception("wtf")

    def __eq__(self, __value):
        return self.cards == __value.cards
    
    def __lt__(self, __value):
        if self.rank < __value.rank:
            return True
        elif self.rank > __value.rank:
            return False
        for i in range(5):
            if self.cards[i] < __value.cards[i]:
                return True
            elif self.cards[i] > __value.cards[i]:
                return False
        return False
    
    def __gt__(self, __value):
        if self.rank > __value.rank:
            return True
        elif self.rank < __value.rank:
            return False
        for i in range(5):
            if self.cards[i] > __value.cards[i]:
                return True
            elif self.cards[i] < __value.cards[i]:
                return False
        return False
    
    def __le__(self, __value):
        if self.rank < __value.rank:
            return True
        elif self.rank > __value.rank:
            return False
        for i in range(5):
            if self.cards[i] < __value.cards[i]:
                return True
            elif self.cards[i] > __value.cards[i]:
                return False
        return True
    
    def __ge__(self, __value):
        if self.rank > __value.rank:
            return True
        elif self.rank < __value.rank:
            return False
        for i in range(5):
            if self.cards[i] > __value.cards[i]:
                return True
            elif self.cards[i] < __value.cards[i]:
                return False
        return True
        

def insert(l1, x):
    if l1 == []:
        return [x]
    elif len(l1) == 1:
        if x < l1[0]:
            return [x, l1[0]]
        return [l1[0], x]
    
    imid = int(len(l1)/2)
    if x < l1[imid]:
        return insert(l1[:imid], x) + l1[imid:]
    else:
        return l1[:imid] + insert(l1[imid:], x)

## result1

def result1(L):
    L_hand = [Hand(card[0], int(card[1])) for card in L]
    L_sort = []
    while L_hand:
        h = L_hand.pop()
        L_sort = insert(L_sort, h)
    score = 0
    for i in range(len(L_sort)):
        score += (i+1)*L_sort[i].bid
    return score

## restult2

def result2(L):
    L_hand = [Hand(card[0], int(card[1]), True) for card in L]
    L_sort = []
    while L_hand:
        h = L_hand.pop()
        L_sort = insert(L_sort, h)
    score = 0
    for i in range(len(L_sort)):
        score += (i+1)*L_sort[i].bid
    return score