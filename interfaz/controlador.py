from grafo.grafo import Grafo
from grafo.algoritmos import AlgoritmosGrafos
import networkx as nx

class ControladorGrafo:
    def __init__(self):
        self.grafo_actual = None
        self.historial = []
    
    def crear_grafo(self):
        self.grafo_actual = Grafo()
        return self.grafo_actual
    
    def agregar_vertice(self, etiqueta):
        if self.grafo_actual:
            return self.grafo_actual.agregar_vertice(etiqueta)
        return None
    
    def agregar_arista(self, origen, destino, peso):
        if self.grafo_actual:
            return self.grafo_actual.agregar_arista(origen, destino, peso)
        return False
    
    def ejecutar_algoritmo(self, algoritmo, **kwargs):
        """Ejecutar algoritmo sobre el grafo actual"""
        if not self.grafo_actual:
            return None
        
        if algoritmo == 'bfs':
            return AlgoritmosGrafos.bfs(self.grafo_actual, kwargs.get('inicio'))
        elif algoritmo == 'dfs':
            return AlgoritmosGrafos.dfs(self.grafo_actual, kwargs.get('inicio'))
        
        return None
    
    def exportar_a_networkx(self):
        grafo = nx.Graph()
        for vertice in self.grafo_actual.vertices:
            grafo.add_node(vertice.etiqueta)
        for aristas in self.grafo_actual.aristas:
            grafo.add_edge(aristas.origen.etiqueta, aristas.destino.etiqueta, weight=aristas.peso)
        return grafo
