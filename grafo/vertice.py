class Vertice:
    def __init__(self, id, etiqueta=None):
        self.id = id
        self.etiqueta = etiqueta or f"V{id}"
        self.vecinos = set()
        self.grado = 0
    
    def agregar_vecino(self, vertice_id, peso):
        self.grado += 1
        
        self.vecinos.add((vertice_id, peso))
    
    def obtener_grado(self):
        return self.grado
    
    def __str__(self):
        return f"({self.id}, '{self.etiqueta}')"
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        return isinstance(other, Vertice) and self.id == other.id