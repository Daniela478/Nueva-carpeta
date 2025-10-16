from grafo.vertice import Vertice
from grafo.arista import Arista

class Grafo:
    def __init__(self):
        self.vertices = []
        self.aristas = []
        self.contador_id_vert = 1
        self.contador_id_ari = 0
    
    def agregar_vertice(self, etiqueta=None):
        vertice_id = self.contador_id_vert
        vertice = Vertice(vertice_id, etiqueta)
        self.vertices.append(vertice)
        self.contador_id_vert += 1
        return vertice_id
    
    def agregar_arista(self, origen, destino, peso=1, etiqueta=None):
        origen = self.obtener_etiqueta_vertice(origen)
        destino = self.obtener_etiqueta_vertice(destino)
        arista_id = self.contador_id_ari

        if origen is None or destino is None:
            raise ValueError("Vértices no existen")
        
        arista = Arista(arista_id, origen, destino, peso, etiqueta)
        self.aristas.append(arista)
        self.contador_id_ari += 1
        
        # Agregar vecinos
        indice_vertice_origen = self.vertices.index(origen)
        indice_vertice_destino = self.vertices.index(destino)
        self.vertices[indice_vertice_origen].agregar_vecino(destino, peso)
        self.vertices[indice_vertice_destino].agregar_vecino(origen, peso)
    
    def eliminar_vertice(self, vertice_id):
        if vertice_id in self.vertices:
            # Eliminar aristas relacionadas
            self.aristas = [a for a in self.aristas 
                          if a.origen != vertice_id and a.destino != vertice_id]
            del self.vertices[vertice_id]
    
    def eliminar_arista(self, origen, destino):
        self.aristas = [a for a in self.aristas 
                       if not (a.origen == origen and a.destino == destino)]
    
    def obtener_etiqueta_vertice(self, etiqueta):
        for vertice in self.vertices:
            if vertice.etiqueta == etiqueta:
                return vertice
        return None

    def obtener_vertices(self):
        return self.vertices
    
    def obtener_aristas(self):
        return self.aristas
    
    def existe_arista(self, origen, destino):
        return any(a.origen == origen and a.destino == destino 
                  for a in self.aristas)
    
    def obtener_vecinos(self, etiqueta):
        vertice = self.obtener_etiqueta_vertice(etiqueta)
        return vertice.vecinos if vertice else set()

    def __str__(self):
        tipo = "Grafo"
        return f"{tipo} con {len(self.vertices)} vértices y {len(self.aristas)} aristas"
    
    def imprimir_vertices(self):
        print(f'los vertices son:')
        for vertice in self.vertices:
            print(f'vertice: {vertice}')

    def imprimir_aristas(self):
        print('Las aristan son:')
        for arista in self.aristas:
            print(arista)