import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Visualizador:
    def __init__(self, layout='spring'):
        self.figura, self.ax = plt.subplots(figsize=(12, 8))
        self.posiciones = None
        self.layout_tipo = layout

    
    def dibujar_grafo(self, grafo_personalizado):
        grafo = nx.Graph()

        # Agregar nodos
        for vertice in grafo_personalizado.vertices:
            grafo.add_node(vertice.etiqueta)

        # Agregar aristas
        for arista in grafo_personalizado.aristas:
            grafo.add_edge(arista.origen.etiqueta, arista.destino.etiqueta, weight=arista.peso)

        if self.posiciones is None:
            if self.layout_tipo == 'spring':
                self.posiciones = nx.spring_layout(grafo, k=2, iterations=50)

        # Limpiar el eje antes de dibujar
        self.ax.clear()

        # Dibujar nodos
        nx.draw_networkx_nodes(grafo, self.posiciones, ax=self.ax,
                            node_size=800, node_color='lightblue',
                            edgecolors='black', linewidths=2)

        # Dibujar aristas
        nx.draw_networkx_edges(grafo, self.posiciones, ax=self.ax,
                            edge_color='gray', width=2)

        # Dibujar etiquetas de nodos
        labels = {n: n for n in grafo.nodes()}
        nx.draw_networkx_labels(grafo, self.posiciones, ax=self.ax,
                                labels=labels, font_size=10, font_weight='bold')

        # Dibujar pesos de aristas
        edge_labels = {(u, vertice): f"{d['weight']}" for u, vertice, d in grafo.edges(data=True)}
        nx.draw_networkx_edge_labels(grafo, self.posiciones, ax=self.ax,
                                    edge_labels=edge_labels, font_size=8)

        self.ax.set_title(f"Grafo - {len(grafo.nodes())} nodos, {len(grafo.edges())} aristas",
                        fontsize=14, fontweight='bold')
        self.ax.set_axis_off()
        plt.tight_layout()

    
    def mostrar(self):
        """Mostrar la visualización"""
        plt.show()
