
class Buffer:
    def __init__(self):
        self.buffer = ""

    def read(self):
        temp = self.buffer.strip()
        self.buffer = ""
        return temp

    def append(self, char):
        self.buffer += char
    
    def not_empty(self):
        return bool(self.buffer)