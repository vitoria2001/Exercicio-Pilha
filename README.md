class Pilha:
  def __init__(self):
    self._itens = []
    
  def isEmpdy(self):
        return self.items == 0

  def push(self, item):
    self.itens.append(item)
    
  def pop(self, item):
    self.itens.pop(item)
    
  def peek(self):
    return self.items[len(self.items)-1]

  def lenght(self):
    return len(self.items)

pilha = Pilha()

