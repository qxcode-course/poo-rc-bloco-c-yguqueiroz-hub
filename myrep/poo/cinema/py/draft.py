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