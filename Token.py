
class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
    
    def __str__(self):
        return self.valor