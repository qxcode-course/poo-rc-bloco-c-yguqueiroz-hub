import sys

class Market:
    def __init__(self, num_counters: int):
        self.counters = [None] * num_counters
        self.waiting = []

    def __str__(self) -> str:
        counters_str = [("----" if p is None else str(p)) for p in self.counters]
        waiting_str = [str(p) for p in self.waiting]

        return (f"Caixas: [{', '.join(counters_str)}]/n"
                f"Espera: [{', '.join(waiting_str)}]")
    
    def arrive(self, person: Person):
        self.waiting.append(person)

    def call(self, index: int):
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return
        
        if not self.waiting:
            print("fail: sem clientes")
            return
        
        if self.counters[index] is not None:
            print("fail: caixa ocupado")
            return
        
        person = self.waiting.pop(0)
        self.counters[index] = person

    def finish(self, index: int) -> Person | None:

        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return None
        
        if self.counters[index] is None:
            print("fail: caixa vazio")
            return None
        
        person = self.counters[index]
        self.counters[index] = None
        return person
    
class Person:

    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
    

def main():
    market = Market(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        print(f"${line}")
        ui = line.split()
        cmd = ui[0]

        try:
             if cmd == "end":
                 break
             elif cmd == "init":
                 market = Market(int(ui[1