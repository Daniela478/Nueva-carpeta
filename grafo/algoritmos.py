from collections import deque
from grafo import Grafo

class AlgoritmosGrafos:
    @staticmethod
    def bfs(grafo, inicio):
        """Búsqueda en amplitud"""
        visitados = set()
        cola = deque([inicio])
        resultado = []
        
        while cola:
            vertice_id = cola.popleft()
            if vertice_id not in visitados:
                visitados.add(vertice_id)
                resultado.append(vertice_id)
                
                for vecino, _ in grafo.obtener_vecinos(vertice_id):
                    if vecino not in visitados:
                        cola.append(vecino)
        
        return resultado
    
    @staticmethod
    def dfs(grafo, inicio):
        """Búsqueda en profundidad"""
        visitados = set()
        resultado = []
        
        def _dfs(vertice_id):
            if vertice_id not in visitados:
                visitados.add(vertice_id)
                resultado.append(vertice_id)
                
                for vecino, _ in grafo.obtener_vecinos(vertice_id):
                    _dfs(vecino)
        
        _dfs(inicio)
        return resultado
    
    @staticmethod
    def prim(grafo, inicio=None):
        """Algoritmo de Prim (sin heapq). Devuelve lista de Arista del MST y muestra su ponderación."""
        if not grafo.vertices:
            print("Grafo vacío.")
            return []

        # Permitir pasar etiqueta o Vertice; si no se pasa, tomar el primero.
        if inicio is None:
            inicio_vert = grafo.vertices[0]
        else:
            inicio_vert = grafo.obtener_etiqueta_vertice(inicio) if isinstance(inicio, str) else inicio
            if inicio_vert is None:
                inicio_vert = grafo.vertices[0]

        visitados = {inicio_vert}
        arbol_generador = []
        ponderacion = 0

        # Mientras no hayamos visitado todos los vértices intentamos agregar la arista mínima
        while len(visitados) < len(grafo.vertices):
            mejor_arista = None
            mejor_peso = float('inf')
            # Buscamos la arista de menor peso que conecte visitados con no visitados
            for v in visitados:
                for vecino, peso in v.vecinos:
                    if vecino not in visitados and peso < mejor_peso:
                        mejor_peso = peso
                        mejor_arista = (v, vecino, peso)

            if mejor_arista is None:
                # El grafo no es conexo
                print("El grafo no es conexo. No se puede construir un MST que cubra todos los vértices.")
                break

            origen, destino, peso = mejor_arista

            # Buscar la arista real en grafo.aristas (considerando no dirigido)
            ar = next((a for a in grafo.aristas
                       if ((a.origen == origen and a.destino == destino) or
                           (a.origen == destino and a.destino == origen)) and a.peso == peso),
                      None)

            # Si no se encuentra la arista (por alguna razón), crear una representación simple
            if ar is None:
                from arista import Arista
                ar = Arista(-1, origen, destino, peso, etiqueta=None)

            arbol_generador.append(ar)
            ponderacion += peso
            visitados.add(destino)

        print(f"Ponderacion: {ponderacion}")
        print(f"Arbol generador: {arbol_generador}")
        return arbol_generador
    
    @staticmethod
    def kruskal(grafo):
        """Algoritmo de Kruskal para la busqueda de arboles generadores optimos de un grafo."""
        aristas_disponibles = grafo.aristas.copy()     # Copia de lista de aristas disp. en el grafo.
        aristas_visitadas = []                         # Lista con aristas utilizadas.
        arbol_generador = []                           # Lista con aristas que forman el arbol optimo.
        bosque_inicial = [{v} for v in grafo.vertices] # Lista que alberga conjuntos formados por los vertices del grafo.
        ponderacion = 0                                # Var. de control para conocer la ponderacion.

        # Mostramos el bosque inicial y el numero de elementos que posee.
        print(f"Bosque actual: {bosque_inicial}...numero de elementos: {len(bosque_inicial)}")

        # NOTA: Inicialmente, bosque_inicial posee conjuntos separados, cada uno con un solo vertice.
        #       La idea es unir estos conjuntos a medida que las aristas conectan sus vertices, formando
        #       árboles pequeños poco a poco (agugugaga)...
        #       Esto nos permite identificar ciclos: si una arista conecta dos vértices en un mismo árbol
        #       podemos formar un ciclo. Si conecta vértices de árboles distintos, podemos construir un 
        #       árbol más grande sin el peligro de provocar ciclos.

        while len(aristas_visitadas) < (len(grafo.vertices) - 1):

            # Tomamos la arista de menor ponderación.
            arista_menor = min(aristas_disponibles, key=lambda a: a.peso)

            origen, destino = arista_menor.obtener_vertices() # Obtenemos los vértices que conecta.

            # Vemos que vértices se están agarrando.
            print(origen)
            print(destino) 

            # Dado que iremos uniendo los conjuntos de vértices, el número de elementos en bosque_inicial
            # no será el mismo. Por eso recorremos por índice los conjuntos que contenga.
            for i in range(len(bosque_inicial)):
                if origen in bosque_inicial[i]:  # Vemos si el origen está en el conjunto en la posición "i".
                    indice_primer_vertice = i
                if destino in bosque_inicial[i]:  # Vemos si el destino está en el conjunto en la posición "i".
                    indice_segundo_vertice = i

            # Si los conjuntos donde se encuentran el origen y el destino son disjuntos y la arista tomada no fue visitada...
            if bosque_inicial[indice_primer_vertice].isdisjoint(bosque_inicial[indice_segundo_vertice]) and arista_menor not in aristas_visitadas:
                
                # Unimos los conjuntos de vértices, sobreescribiendo uno de los ya existentes en
                # bosque_inicial con el nuevo conjunto.
                bosque_inicial[indice_primer_vertice] = bosque_inicial[indice_primer_vertice].union(bosque_inicial[indice_segundo_vertice])
                del bosque_inicial[indice_segundo_vertice] # Eliminamos uno de los conjuntos "menores".

                arbol_generador.append(arista_menor)     # Añadimos la arista al árbol generador.
                aristas_visitadas.append(arista_menor)   # Añadimos la arista a las ya visitadas.
                aristas_disponibles.remove(arista_menor) # Quitamos la arista de las disponibles.

                # Mostramos cómo va quedando el bosque y los conjuntos que tiene...
                print(f"Bosque actual: {bosque_inicial}...numero de elementos: {len(bosque_inicial)}")

            else:
                print("La arista tomada provoca un ciclo. La descartamos.")
                aristas_disponibles.remove(arista_menor) # Eliminamos la arista de las disponibles.
                continue                                 # "Continuamos" a la siguiente iteración.

        # Calculamos la ponderación.
        for a in aristas_visitadas:
            ponderacion += a.peso

        print(f"Arbol generador: {arbol_generador}") # Mostramos el árbol generador.
        print(f"Ponderacion: {ponderacion}")         # Mostramos su ponderación.
        return arbol_generador
