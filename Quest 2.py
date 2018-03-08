class Pilha:
    def __init__ (self):
        self.items = []

    def isVazio (self):
         if (len(self._itens) == 0):
           return "Vazio"

    def push (self, item):
        if item not in self.items:
             self._itens.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def lenght(self):
        return len(self.items)
        
pilha = Pilha()
