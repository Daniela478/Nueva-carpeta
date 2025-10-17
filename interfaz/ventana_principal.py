import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importar nuestros módulos existentes
from interfaz.controlador import ControladorGrafo
from interfaz.visualizador import Visualizador


# Estilos básicos
COLOR_FONDO = "#ecf0f1"
COLOR_PRIMARIO = "#2c3e50"
COLOR_ACENTO = "#3498db"
COLOR_TEXTO = "#474f57"
COLOR_TEXTO_CLARO = "#ffffff"

FUENTE_TITULO = ("Arial", 20, "bold")
FUENTE_NORMAL = ("Arial", 14, "bold")
FUENTE_MONOSPACE = ("Courier New", 9)

class VentanaPrincipal:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("Proyecto de Grafo")
        self.pantalla.geometry("1280x920")
        self.pantalla.configure(bg=COLOR_FONDO)
        
        # Usar el controlador existente
        self.controlador = ControladorGrafo()
        self.visualizador = Visualizador(layout='spring')

        self._cargar_grafo_inicial()  # Primero carga el grafo
        self.configurar_interfaz()    # Luego configura la interfaz y dibuja
        self.visualizador.dibujar_grafo(self.controlador.grafo_actual)






        
    def configurar_interfaz(self):
        # Crear Pestañas
        self.pestañas = ttk.Notebook(self.pantalla)
        self.pestañas.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña 1: Creación de Grafos
        self.pestaña1 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña1, text="Grafo actual")

        self.pestaña2 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña2, text="Algoritmo BFS")

        self.pestaña3 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña3, text="Algoritmo DFS")
        
        self.pestaña4 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña4, text='Algoritmo Kruskal')
        
        self.pestaña5 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña5, text='Algoritmo Prim')
        
        # Configurar cada pestaña
        self.configurar_pestaña_creacion()
        self.configurar_pestaña_bfs()
        self.configurar_pestaña_dfs()
        self.configurar_pestaña_kruskal()
        self.configurar_pestaña_prim()
        self.insertar_grafo_en_pestaña(self.pestaña1)
        self.insertar_grafo_en_pestaña(self.pestaña2)  # BFS
        self.insertar_grafo_en_pestaña(self.pestaña3)  # DFS
        self.insertar_grafo_en_pestaña(self.pestaña4)  # Kruskal
        self.insertar_grafo_en_pestaña(self.pestaña5)  # Prim

        
    def configurar_pestaña_creacion(self):
        # Frame principal
        ventana_grafo = ttk.Frame(self.pestaña1)
        ventana_grafo.pack(fill='both', expand=True, padx=20, pady=20)

        
        # Título
        titulo = tk.Label(ventana_grafo, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Nuestro Grafo es el siguiente")
        titulo.pack(pady=10)
        # Frame para mostrar el grafo
        self.pantalla_grafo_visto = ttk.Frame(self.pestaña1)
        self.pantalla_grafo_visto.pack(fill='both', expand=True, padx=10, pady=10)

        
        # Botones de acción
        botones_principales = ttk.Frame(ventana_grafo)
        botones_principales.pack(pady=20)
        
        boton_agregar_vertice = tk.Button(botones_principales, bg=COLOR_ACENTO, fg=COLOR_TEXTO_CLARO,
                               font=FUENTE_NORMAL, text="Agregar vertice", 
                               command=self.agregar_vertice)
        boton_agregar_vertice.pack(side='left', padx=10, ipadx=10, ipady=10)
        
        boton_agregar_arista = tk.Button(botones_principales, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Agregar arista", 
                              command=self.agregar_arista)
        boton_agregar_arista.pack(side='left', padx=10, ipadx=10, ipady=10)

        boton_modificar_vertice = tk.Button(botones_principales, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Modificar vertice", 
                              command=self.modificar_vertice)
        boton_modificar_vertice.pack(side='left', padx=10, ipadx=10, ipady=10)

        boton_modificar_arista = tk.Button(botones_principales, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Modificar arista", 
                              command=self.modificar_arista)
        boton_modificar_arista.pack(side='left', padx=10, ipadx=10, ipady=10)

        boton_eliminar_vertice = tk.Button(botones_principales, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Eliminar vertice", 
                              command=self.eliminar_vertice)
        boton_eliminar_vertice.pack(side='left', padx=10, ipadx=10, ipady=10)

        boton_eliminar_arista = tk.Button(botones_principales, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Eliminar arista", 
                              command=self.eliminar_arista)
        boton_eliminar_arista.pack(side='left', padx=10, ipadx=10, ipady=10)

    def configurar_pestaña_bfs(self):
        ventana_grafo = ttk.Frame(self.pestaña2)
        ventana_grafo.pack(fill='both', expand=True, padx=20, pady=20)
        titulo = tk.Label(ventana_grafo, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Algoritmo BSF")
        titulo.pack(pady=10)

        self.pantalla_grafo_visto = ttk.Frame(self.pestaña2)
        self.pantalla_grafo_visto.pack(fill='both', expand=True, padx=10, pady=10)        
    def configurar_pestaña_dfs(self):
        ventana_grafo = ttk.Frame(self.pestaña3)
        ventana_grafo.pack(fill='both', expand=True, padx=20, pady=20)
        titulo = tk.Label(ventana_grafo, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Algoritmo DFS")
        titulo.pack(pady=10)
        self.pantalla_grafo_visto = ttk.Frame(self.pestaña3)
        self.pantalla_grafo_visto.pack(fill='both', expand=True, padx=10, pady=10)        
    def configurar_pestaña_kruskal(self):
        ventana_grafo = ttk.Frame(self.pestaña4)
        ventana_grafo.pack(fill='both', expand=True, padx=20, pady=20)
        titulo = tk.Label(ventana_grafo, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Algoritmo Kruskal")
        titulo.pack(pady=10)
        self.pantalla_grafo_visto = ttk.Frame(self.pestaña4)
        self.pantalla_grafo_visto.pack(fill='both', expand=True, padx=10, pady=10)
    def configurar_pestaña_prim(self):
        ventana_grafo = ttk.Frame(self.pestaña5)
        ventana_grafo.pack(fill='both', expand=True, padx=20, pady=20)
        titulo = tk.Label(ventana_grafo, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Algoritmo Prim")
        titulo.pack(pady=10)
        self.pantalla_grafo_visto = ttk.Frame(self.pestaña5)
        self.pantalla_grafo_visto.pack(fill='both', expand=True, padx=10, pady=10)


    def insertar_grafo_en_pestaña(self, pestaña):
        pantalla = ttk.Frame(pestaña)
        pantalla.pack(fill='both', expand=True, padx=10, pady=10)

        self.visualizador.dibujar_grafo(self.controlador.grafo_actual)

        canvas = FigureCanvasTkAgg(self.visualizador.figura, master=pantalla)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)



        
    def visualizar_grafo(self):
        if not self.controlador.grafo_actual:
            messagebox.showwarning("Advertencia", "No tenemos grafo :(.")
            return

        for widget in self.pantalla_grafo_visto.winfo_children():
            widget.destroy()

        self.visualizador.dibujar_grafo(self.controlador.grafo_actual)


        canvas = FigureCanvasTkAgg(self.visualizador.figura, master=self.pantalla_grafo_visto)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)



    def agregar_vertice(self):
        pass
    
    def agregar_arista(self):
        pass
    def eliminar_vertice(self):
        pass
    def eliminar_arista(self):
        pass
    def modificar_vertice(self):
        pass
    def modificar_arista(self):
        pass
    
    def _cargar_grafo_inicial(self):
        # grafo = self.controlador.crear_grafo()
        self.controlador.crear_grafo()
        
        nombres_vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P']
        for n in nombres_vertices:
            self.controlador.grafo_actual.agregar_vertice(n)

        self.controlador.grafo_actual.agregar_arista("A", "B", 8)
        self.controlador.grafo_actual.agregar_arista("A", "D", 5)
        self.controlador.grafo_actual.agregar_arista("A", "E", 4)
        self.controlador.grafo_actual.agregar_arista("B", "C", 3)
        self.controlador.grafo_actual.agregar_arista("B", "F", 4)
        self.controlador.grafo_actual.agregar_arista("B", "E", 6)
        self.controlador.grafo_actual.agregar_arista("C", "F", 13)
        self.controlador.grafo_actual.agregar_arista("C", "G", 7)
        self.controlador.grafo_actual.agregar_arista("D", "E", 1)
        self.controlador.grafo_actual.agregar_arista("D", "I", 2)
        self.controlador.grafo_actual.agregar_arista("D", "H", 3)
        self.controlador.grafo_actual.agregar_arista("E", "I", 2)
        self.controlador.grafo_actual.agregar_arista("E", "F", 3)
        self.controlador.grafo_actual.agregar_arista("F", "G", 1)
        self.controlador.grafo_actual.agregar_arista("F", "I", 3)
        self.controlador.grafo_actual.agregar_arista("F", "K", 22)
        self.controlador.grafo_actual.agregar_arista("G", "K", 1)
        self.controlador.grafo_actual.agregar_arista("G", "L", 6)
        self.controlador.grafo_actual.agregar_arista("H", "M", 13)
        self.controlador.grafo_actual.agregar_arista("H", "I", 13)
        self.controlador.grafo_actual.agregar_arista("I", "K", 7)
        self.controlador.grafo_actual.agregar_arista("I", "P", 20)
        self.controlador.grafo_actual.agregar_arista("I", "N", 2)
        self.controlador.grafo_actual.agregar_arista("I", "M", 9)
        self.controlador.grafo_actual.agregar_arista("K", "L", 7)
        self.controlador.grafo_actual.agregar_arista("K", "P", 6)
        self.controlador.grafo_actual.agregar_arista("L", "P", 15)
        self.controlador.grafo_actual.agregar_arista("M", "N", 1)
        self.controlador.grafo_actual.agregar_arista("N", "P", 14)
    