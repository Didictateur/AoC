class Condition:
    def __init__(self, input: str) -> None:
        if ":" in input:
            input = input.split(":")
            destination = input[1]
            input = input[0]
            parameters = {"x": 0,  "m": 1, "a": 2, "s": 3}
            if "<" in input:
                input = input.split("<")
                self.value = lambda wf: (wf[parameters[input[0]]] < int(input[1]), destination)
            elif ">" in input:
                input = input.split(">")
                self.value = lambda wf: (wf[parameters[input[0]]] > int(input[1]), destination)
            else:
                raise Exception("Invalid condition")
        else:
            self.value = lambda wf: (True, input)

class Rule:
    def __init__(self, input: str) -> None:
        input = input.split("{")
        self.name = input[0]
        input = input[1][:-1].split(",")
        self.conditions = [Condition(c) for c in input]
    
    def next(self, wf: list) -> str:
        for c in self.conditions:
            if c.value(wf)[0]:
                return c.value(wf)[1]
        raise Exception("No condition met")

def find_rule(L, name):
    for r in L:
        if r.name == name:
            return r
    raise Exception(f"No rule {name} found")

## result1

def result1(L):
    L = [l[0] for l in L]
    L_rules_brute = [l for l in L if l[0] != "{"]
    L_workflows_brute = [l for l in L if l[0] == "{"]

    L_rules = [Rule(r) for r in L_rules_brute]
    L_workflows_brute = [l[1:-1].split(",") for l in L_workflows_brute]
    L_workflows = []
    for l in L_workflows_brute:
        L_workflows.append([])
        for wf in l:
            wf = wf.split("=")
            L_workflows[-1].append(int(wf[1]))
    
    nb_accpeted = 0
    for wf in L_workflows:
        current_rule = "in"
        while current_rule not in {"A", "R"}:
            current_rule = find_rule(L_rules, current_rule).next(wf)
        if current_rule == "A":
            nb_accpeted += sum(wf)

    return nb_accpeted
    
## restult2

def result2(L):
    L = [l[0] for l in L]
    L_rules_brute = [l for l in L if l[0] != "{"]
    L_workflows_brute = [l for l in L if l[0] == "{"]

    L_rules = [Rule(r) for r in L_rules_brute]
    L_workflows_brute = [l[1:-1].split(",") for l in L_workflows_brute]
    L_workflows = []
    for a in range(4000):
        for b in range(4000):
            for c in range(4000):
                for d in range(4000):
                    L_workflows.append([a, b, c, d])
    
    nb_accpeted = 0
    for wf in L_workflows:
        current_rule = "in"
        while current_rule not in {"A", "R"}:
            current_rule = find_rule(L_rules, current_rule).next(wf)
        if current_rule == "A":
            nb_accpeted += 1

    return nb_accpeted