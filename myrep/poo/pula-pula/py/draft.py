import sys
from collections import deque 

class Criança:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    def __str__(self) -> str:
        return f"{self.name}:{self.age}"
    
class Trampolim:
    def __init__(self):
        self.waiting = deque()
        self.playing = deque()

    def arrive(self, name: str, age: int):
        criança = Criança(name, age)
        self.waiting.append(criança)

    def enter(self):
        if not self.waiting:
            return
        
        criança = self.waiting.popleft()
        self.playing.append(criança)

    def leave(self):
        if not self.playing:
            return
        criança = self.playing.popleft()
        self.waiting.append(criança)

    def remove(self,name: str):
        for criança in self.waiting:
            if criança.name == name:
                self.waiting.remove(criança)
                return
            
        for criança in self.playing:
            if criança.name == name:
                self.playing.remove(criança)
                return
            
        print(f"fail: {name} nao esta no pula-pula")

    def __str__(self) -> str:
        waiting_str = ", ".join([str(criança) for criança in  reversed(self.waiting)])
        playing_str = ", ".join([str(criança) for criança in reversed(self.playing)])
        return f"[{waiting_str}] => [{playing_str}]"

def main():
     
    trampolim = Trampolim()

    for line in sys.stdin:
         line = line.strip()
         if not line:
             continue
         print(f"${line}")

         parts = line.split()
         cmd = parts[0]
         
         if cmd == 'end':
             break
         elif cmd == 'show':
             print(trampolim)
         elif cmd == 'arrive':
             trampolim.arrive(parts[1], int(parts[2]))
         elif cmd == 'enter':
             trampolim.enter()
         elif cmd == 'leave':
             trampolim.leave()
         elif cmd == 'remove':
             trampolim.remove(parts[1])
         else:
             print(f"fail: comando'{cmd}' inválido")
if __name__ == "__main__":
    main()