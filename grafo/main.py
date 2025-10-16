from grafo import Grafo

grafo1 = Grafo()
grafo1.agregar_vertice('A')
grafo1.agregar_vertice('B')
grafo1.agregar_arista('A', 'B', 5, 'a1')
grafo1.imprimir_vertices()
grafo1.imprimir_aristas()

grafo1.obtener_vecinos('A')