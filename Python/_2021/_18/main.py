class Tree:
    def __init__(self, data: str, layout: int=0) -> None:
        self.LeftTree = None
        self.RightTree = None

        count = 0
        i = 0
        while data[i] != "," or count != 0:
            i += 1
            if data[i] == "[":
                count += 1
            elif data[i] == "]":
                count -= 1
        left = data[1:i]
        right = data[i+1:-1]

        try:
            self.LeftTree = int(left)
        except:
            self.LeftTree = Tree(left)
        
        try:
            self.RightTree = int(right)
        except:
            self.RightTree = Tree(right)
    
    def __str__(self) -> str:
        return f"[{self.LeftTree},{self.RightTree}]"
    
    def get_height(self) -> int:
        if type(self.LeftTree) == int:
            if type(self.RightTree) == int:
                return 0
            else:
                return 1+self.RightTree.get_height()
        else:
            if type(self.RightTree) == int:
                return 1+self.LeftTree.get_height()
            else:
                return 1+max(self.LeftTree.get_height(), self.RightTree.get_height())
    
    def add(self, value: int, left=True):
        if left:
            if type(self.LeftTree) == int:
                self.LeftTree += value
            else:
                self.LeftTree.add(value, left)
        else:
            if type(self.RightTree) == int:
                self.RightTree += value
            else:
                self.RightTree.add(value, left)
    
    def find_who_to_explose(self, n: int): # True = 'left'
        if type(self.LeftTree) == int and type(self.RightTree) == int:
            if n >= 4:
                return [True, []]
            return [False, []]
        
        if type(self.LeftTree) != int and type(self.RightTree) == int:
            result = self.LeftTree.find_who_to_explose(n+1)
            if result[0]:
                return [True, [True] + result[1]]
            return [False, []]
        
        if type(self.LeftTree) == int and type(self.RightTree) != int:
            result = self.RightTree.find_who_to_explose(n+1)
            if result[0]:
                return [True, [False] + result[1]]
            return [False, []]
        
        else:
            result = self.LeftTree.find_who_to_explose(n+1)
            if result[0]:
                return [True, [True] + result[1]]
            
            result = self.RightTree.find_who_to_explose(n+1)
            if result[0]:
                return [True, [False] + result[1]]
            return [False, []]
    
    def exploses_one(self, L: list[bool], i: int):
        if i == len(L):
            return [self.LeftTree, self.RightTree]
        
        if L[i]:
            result = self.LeftTree.exploses_one(L, i+1)
            if len(result) == 2:
                self.LeftTree = 0
                if type(self.RightTree) == int:
                    self.RightTree += result[1]
                else:
                    self.RightTree.add(result[1], True)
                return [result[0]]
            elif len(result) == 1:
                if L[i+1]:
                    return result
                if type(self.RightTree) == int:
                    self.RightTree += result[0]
                else:
                    self.RightTree.add(result[0], True)
                return []
            else:
                return []
            
        else:
            result = self.RightTree.exploses_one(L, i+1)
            if len(result) == 2:
                self.RightTree = 0
                if type(self.LeftTree) == int:
                    self.LeftTree += result[0]
                else:
                    self.LeftTree.add(result[0], False)
                return [result[1]]
            elif len(result) == 1:
                if not L[i+1]:
                    return result
                if type(self.LeftTree) == int:
                    self.LeftTree += result[0]
                else:
                    self.LeftTree.add(result[0], False)
                return []
            else:
                return []
    
    def exploses(self):
        if self.get_height() >= 4:
            L = self.find_who_to_explose(0)[1]
        self.exploses_one(L, 0)
            
    def split(self) -> bool:
        if type(self.LeftTree) == int:
            if self.LeftTree > 9:
                self.LeftTree = Tree(f"[{self.LeftTree//2},{self.LeftTree-self.LeftTree//2}]")
                return True
        elif self.LeftTree.split():
            return True
        if type(self.RightTree) == int:
            if self.RightTree > 9:
                self.RightTree = Tree(f"[{self.RightTree//2},{self.RightTree-self.RightTree//2}]")
                return True
            return False
        if self.RightTree.split():
            return True
        return False
    
    def magnitude(self) -> int:
        left_v = 0
        rigth_v = 0

        if type(self.LeftTree) == int:
            left_v = self.LeftTree
        else:
            left_v = self.LeftTree.magnitude()

        if type(self.RightTree) == int:
            rigth_v = self.RightTree
        else:
            rigth_v = self.RightTree.magnitude()

        return 3*left_v+2*rigth_v
    
class SnailNumber:
    def __init__(self, data: str) -> None:
        self.tree = Tree(data)
        self.simplify()
    
    def __str__(self) -> str:
        return str(self.tree)
    
    def __add__(self, __value: "SnailNumber") -> "SnailNumber":
        newNumber = SnailNumber(f"[{self},{__value}]")
        newNumber.simplify()
        return newNumber
    
    def get_height(self) -> int:
        return self.tree.get_height()
    
    def simplify(self) -> None:
        changed = True
        while changed:
            changed = False
            if self.get_height() >= 4:
                self.tree.exploses()
                changed = True
            if not changed:
                changed = self.tree.split()
    
    def get_magnitude(self) -> int:
        return self.tree.magnitude()

## result1

def result1(L):
    t = SnailNumber(L[0][0])
    for t_ in L[1:]:
        t += SnailNumber(t_[0])

    return t.get_magnitude()
    
## result2

def result2(L):
    l_t = []
    for t_ in L:
        l_t.append(SnailNumber(t_[0]))
    
    s = 0
    for i in range(len(l_t)):
        for j in range(i, len(l_t)):
            s1 = (l_t[i]+l_t[j]).get_magnitude()
            s2 = (l_t[j]+l_t[i]).get_magnitude()
            s = max(s, s1, s2)
    return s