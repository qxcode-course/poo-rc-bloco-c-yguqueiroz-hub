class Client:
    def __init__(self, id: str, phone: int):
        self.id = id 
        self.phone = phone

    def __str__(self):
        return f"{self.id},{self.phone}"
    
class Theater:
    def __init__(self, capacity: int):
        self.seats = [None] * capacity

    def _verify_index(self, index: int) -> bool:
        return 0 <= index < len(self.seats)
    
    def _search(self, id: str) -> int:
        for i, client in enumerate(self.seats):
            if client is not None:
                if client.id == id:
                    return i 
        return -1
    def reserve(self,id: str, phone: int, index: int):
        if not self._verify_index(index):
            print("fail: cadeira nao existe")
            return
        
        if self.seat[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        
        if self._search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return
        
        self.seats[index] = Client(id, phone)

    def cancel(self, id: str):
        index = self._seach(id)
