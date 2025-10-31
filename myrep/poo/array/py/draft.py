import random

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome   

class Onibus:
     def __init__(self, n_cadeiras):
         self.espera = []

         self.cadeiras = []
         for _ in range(n_cadeiras):
             self.cadeiras.append(None)

     def __str__(self):
         for p in self.cadeiras:
             if p is not None:
                 cadeiras_str_list.append(str(p))
             else:
                 cadeiras_str_list.append('-')

         cadeiras_fmt = ' '.join(cadeiras_str_list)

         return f"Cadeiras: {cadeiras_fmt} \nEspera: {self.espera}"
     
def get_nome(pessoa):
    return pessoa.nome