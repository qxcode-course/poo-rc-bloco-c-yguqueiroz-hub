class Pessoa:
    def __init__(self) -> None:
        pass    

class Onibus:
     def __init__(self, n_cadeiras: int):
         self.espera: list[Pessoa] = []
         self.cadeiras: list[Pessoa | None] = []
         for _ in range(n_cadeiras):
             self.cadeira.append(None)

     def __str__(self):
         cadeiras = ',' .join[str(x) for x in self.cadeiras]
         return f"Cadeiras: {self.cadeiras}\nEspera:{self.espera}"
     
david = Pessoa("David")
print(david)
onibus = Onibus(5)
print(onibus)