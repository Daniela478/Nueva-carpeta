import matplotlib.pyplot as plt
import networkx
import numpy as np

class Visualizador:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.posiciones = {}
        self.grafo_original = None
        self.grafo_nx = networkx.Graph()
        self.layout = 'spring'
        self.nodos_personalizados = []
    
    def dibujar_grafo(self, grafo, layout='spring'):
        grafo =  networkx.Graph()
        
        for vertice in grafo.obtener_vertices():
            grafo.add_node(vertice.id, label=vertice.etiqueta, datos=vertice.datos)
        
        for arista in grafo.obtener_aristas():
            grafo.add_edge(arista.origen, arista.destino, weight=arista.peso)
        
        if layout == 'spring':
            self.posiciones = networkx.spring_layout(grafo, k=2, iterations=50)
        elif layout == 'circular':
            self.posiciones = networkx.circular_layout(grafo)
        elif layout == 'random':
            self.posiciones = networkx.random_layout(grafo)
        else:
            self.posiciones = networkx.spring_layout(grafo)
        
        self.ax.clear()
        
        networkx.draw_networkx_nodes(grafo, self.posiciones, ax=self.ax, 
                              node_size=800, node_color='lightblue',
                              edgecolors='black', linewidths=2)
        
        if grafo.dirigido:
            networkx.draw_networkx_edges(grafo, self.posiciones, ax=self.ax,
                                  arrowstyle='->', arrowsize=20,
                                  edge_color='gray', width=2)
        else:
            networkx.draw_networkx_edges(grafo, self.posiciones, ax=self.ax,
                                  edge_color='gray', width=2)
        
        labels = {n: grafo.nodes[n]['label'] for n in grafo.nodes()}
        networkx.draw_networkx_labels(grafo, self.posiciones, ax=self.ax, 
                               labels=labels, font_size=10, font_weight='bold')
        
        edge_labels = {(u, v): f"{d['weight']}" for u, v, d in grafo.edges(data=True)}
        networkx.draw_networkx_edge_labels(grafo, self.posiciones, ax=self.ax,
                                    edge_labels=edge_labels, font_size=8)
        
        titulo = "Digrafo" if grafo.dirigido else "Grafo"
        self.ax.set_title(f"{titulo} - {len(grafo.nodes())} nodos, {len(grafo.edges())} aristas",
                         fontsize=14, fontweight='bold')
        self.ax.set_axis_off()
        
        plt.tight_layout()
    
    def mostrar(self):
        """Mostrar la visualización"""
        plt.show()
    
    def guardar_imagen(self, filename='grafo.png'):
        """Guardar la visualización como imagen"""
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Imagen guardada como {filename}")