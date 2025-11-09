import sys

class Grafite:
    
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def get_desgaste_por_folha(self) -> int:
        if self.dureza == "HB":
            return 1
        if self.dureza == "2B":
            return 2
        if self.dureza == "4B":
            return 4
        if self.dureza == "6B":
            return 6
        return 0 
    
    def __str__(self):
        return f"[{self.calibre:.1f}:{self.dureza}:{self.tamanho}]"
    
class Lapiseira:

    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico: Grafite | None = None 
        self.tambor: list[Grafite] = []

    def inserir(self, grafite: Grafite) -> bool:
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
            return False
        
        self.tambor.append(grafite)
        return True
    
    def pull(self) -> bool:
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return False
        
        if not self.tambor:
            print("fail: tambor esta vazio")
            return False
        
        self.bico = self.tambor.pop(0)
        return True
    
    def remove(self) -> bool:
        if self.bico is None:
            print("fail: bico vazio")
            return False
        
        self.bico = None
        return True
    
    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        
        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return
        
        desgaste = self.bico.get_desgaste_por_folha()

        if (self.bico.tamanho - desgaste) < 10:
            print("fail: folha incompleta")
            self.bico.tamanho = 10
        else:
            self.bico.tamanho -= desgaste

    def __repr__(self) -> str:
        bico_str = str(self.bico) if self.bico is not None else "[]"
        tambor_str = "".join(map(str, self.tambor))

        return f"calibre: {self.calibre:.1f}, bico: {bico_str}, tambor: <{tambor_str}>"
 
def main():
    lapiseira = None

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
                lapiseira = Lapiseira(float(ui[1]))
            elif cmd == "insert":
                if lapiseira:
                    grafite = Grafite(float(ui[1]), ui[2], int(ui[3]))
                    lapiseira.inserir(grafite)
                else:
                    print("fail: lapiseira nao iniciada")
            elif cmd == "show":
                if lapiseira:
                    print(lapiseira)
                else:
                    print("fail: lapiseira nao iniciada")
            elif cmd == "pull":
                if lapiseira:
                    lapiseira.pull()
                else:
                    print("fail: lapiseira nao iniciada")
            elif cmd == "remove":
                if lapiseira:
                    lapiseira.remove()
                else:
                    print("fail: lapiseira nao iniciada")
            elif cmd == "write":
                if lapiseira:
                    lapiseira.write()
                else:
                    print("fail: lapiseira nao iniciada")
            else:
                print(f"fail: comando '{cmd}' invalido")
        except IndexError:
            print(f"fail: parametros insuficientes para '{cmd}'")
        except Exception as e:
            print(f"fail: {e}")

if __name__ == "__main__":
    main()