class Arista:
    def __init__(self, id, origen, destino, peso=1, etiqueta=None):
        self.id = id
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.etiqueta = etiqueta if etiqueta else f"A{id}"
    
    def obtener_vertices(self):
        return (self.origen, self.destino)
    
    def __str__(self):
        direccion = "—"
        return f"Arista '{self.etiqueta}' {self.origen} {direccion} {self.destino} (peso: {self.peso})"
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash((self.id, self.origen, self.destino, self.peso))
    
    def __eq__(self, other):
        return (isinstance(other, Arista) and 
                self.id == other.id and
                self.origen == other.origen and
                self.destino == other.destino and
                self.peso == other.peso)