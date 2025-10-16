import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from interfaz.controlador import ControladorGrafo
from interfaz.visualizador import Visualizador


COLOR_FONDO = "#ecf0f1"
COLOR_PRIMARIO = "#2c3e50"
COLOR_ACENTO = "#3498db"
COLOR_TEXTO = "#474f57"
COLOR_TEXTO_CLARO = "#ffffff"

FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_NORMAL = ("Arial", 10)
FUENTE_MONOSPACE = ("Courier New", 9)

class VentanaPrincipal:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.pantalla.title("Proyecto de Grafo")
        self.pantalla.geometry("1200x1200")
        self.pantalla.configure(bg=COLOR_FONDO)
        
        self.controlador = ControladorGrafo()
        self.visualizador = None
        
        self._configurar_interfaz()
        
    def _configurar_interfaz(self):
       
        self.pestañas = ttk.Notebook(self.pantalla)
        self.pestañas.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.pestaña1 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña1, text="Grafo actual")

        self.pestaña2 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña2, text="Algoritmo bss")

        self.pestaña3 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña3, text="Algoritmo bfs")
        
        
        self.pestaña4 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña4, text='Algoritmo kruskal')
        

        self.pestaña5 = ttk.Frame(self.pestañas)
        self.pestañas.add(self.pestaña5, text='Algoritmo kruskal')
        
        self._configurar_pestaña_creacion()
        self._configurar_pestaña_teoria()
        self._configurar_pestaña_visualizacion()
        
    def _configurar_pestaña_creacion(self):

        main_frame = ttk.Frame(self.pestaña1)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        titulo = tk.Label(main_frame, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Nuestro Grafo es el siguiente")
        titulo.pack(pady=10)
        

        
        self.texto_enunciado = scrolledtext.ScrolledText(
            main_frame, 
            bg="white", fg=COLOR_TEXTO, font=FUENTE_NORMAL,
            height=8, width=80, relief="sunken", bd=1
        )
        self.texto_enunciado.pack(pady=10, fill='x')
        
        frame_botones = ttk.Frame(main_frame)
        frame_botones.pack(pady=20)
        
        boton_agregar_vertice = tk.Button(frame_botones, bg=COLOR_ACENTO, fg=COLOR_TEXTO_CLARO,
                               font=FUENTE_NORMAL, text="Agregar vertice", 
                               command=self._procesar_enunciado)
        boton_agregar_vertice.pack(side='left', padx=10)
        
        boton_agregar_arista = tk.Button(frame_botones, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Agregar arista", 
                              command=self._limpiar_enunciado)
        boton_agregar_arista.pack(side='left', padx=10)

        boton_modificar_vertice = tk.Button(frame_botones, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Modificar vertice", 
                              command=self._limpiar_enunciado)
        boton_modificar_vertice.pack(side='left', padx=10)

        boton_modificar_arista = tk.Button(frame_botones, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Modificar arista", 
                              command=self._limpiar_enunciado)
        boton_modificar_arista.pack(side='left', padx=10)

        boton_eliminar_arista = tk.Button(frame_botones, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Eliminar vertice", 
                              command=self._limpiar_enunciado)
        boton_eliminar_arista.pack(side='left', padx=10)

        boton_eliminar_arista = tk.Button(frame_botones, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="Eliminar arista", 
                              command=self._limpiar_enunciado)
        boton_eliminar_arista.pack(side='left', padx=10)

        # Área de información del grafo
        self.frame_info = ttk.LabelFrame(main_frame, text="Información del Grafo")
        self.frame_info.pack(pady=10, fill='x')
        
        self.lbl_info = tk.Label(self.frame_info, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                font=FUENTE_NORMAL, text="No hay grafo creado")
        self.lbl_info.pack(pady=10)
        
    def _configurar_pestaña_teoria(self):
        main_frame = ttk.Frame(self.frame_teoria)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        lbl_titulo = tk.Label(main_frame, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Consultas de Teoría de Grafos")
        lbl_titulo.pack(pady=10)

        lbl_consulta = tk.Label(main_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                               font=FUENTE_NORMAL,
                               text="Haz una pregunta sobre teoría de grafos:")
        lbl_consulta.pack(pady=5)
        
        self.entrada_consulta = tk.Entry(main_frame, bg="white", fg=COLOR_TEXTO,
                                       font=FUENTE_NORMAL, width=60, relief="sunken", bd=1)
        self.entrada_consulta.pack(pady=10)
        self.entrada_consulta.bind('<Return>', lambda e: self._responder_consulta())
        
        btn_consultar = tk.Button(main_frame, bg=COLOR_ACENTO, fg=COLOR_TEXTO_CLARO,
                                font=FUENTE_NORMAL, text="🤖 Consultar", 
                                command=self._responder_consulta)
        btn_consultar.pack(pady=10)
        
        # Área de respuesta
        lbl_respuesta = tk.Label(main_frame, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                font=FUENTE_NORMAL, text="Respuesta:")
        lbl_respuesta.pack(pady=5, anchor='w')
        
        self.texto_respuesta = scrolledtext.ScrolledText(
            main_frame, 
            bg="white", fg=COLOR_TEXTO, font=FUENTE_MONOSPACE,
            height=15, width=80, relief="sunken", bd=1, wrap="word"
        )
        self.texto_respuesta.pack(pady=10, fill='both', expand=True)
        self.texto_respuesta.config(state='disabled')
        
    def _configurar_pestaña_visualizacion(self):
        main_frame = ttk.Frame(self.frame_visualizacion)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
       
        lbl_titulo = tk.Label(main_frame, bg=COLOR_FONDO, fg=COLOR_PRIMARIO,
                             font=FUENTE_TITULO, text="Visualización del Grafo")
        lbl_titulo.pack(pady=10)
        
        frame_controles = ttk.Frame(main_frame)
        frame_controles.pack(pady=10, fill='x')
        
        lbl_layout = tk.Label(frame_controles, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                            font=FUENTE_NORMAL, text="Layout:")
        lbl_layout.pack(side='left', padx=5)
        
        self.combo_layout = ttk.Combobox(frame_controles, 
                                       values=['spring', 'circular', 'random'],
                                       width=15)
        self.combo_layout.pack(side='left', padx=5)
        self.combo_layout.set('spring')
        
        btn_visualizar = tk.Button(frame_controles, bg=COLOR_ACENTO, fg=COLOR_TEXTO_CLARO,
                                 font=FUENTE_NORMAL, text="📊 Visualizar", 
                                 command=self._visualizar_grafo)
        btn_visualizar.pack(side='left', padx=10)
        
        btn_guardar = tk.Button(frame_controles, bg="#34495e", fg=COLOR_TEXTO_CLARO,
                              font=FUENTE_NORMAL, text="💾 Guardar Imagen", 
                              command=self._guardar_imagen)
        btn_guardar.pack(side='left', padx=10)
        
        frame_algoritmos = ttk.Frame(main_frame)
        frame_algoritmos.pack(pady=10, fill='x')
        
        lbl_algoritmos = tk.Label(frame_algoritmos, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                 font=FUENTE_NORMAL, text="Algoritmos:")
        lbl_algoritmos.pack(side='left', padx=5)
        
        btn_bfs = tk.Button(frame_algoritmos, bg="#27ae60", fg=COLOR_TEXTO_CLARO,
                          font=FUENTE_NORMAL, text="BFS", 
                          command=lambda: self._ejecutar_algoritmo('bfs'))
        btn_bfs.pack(side='left', padx=5)
        
        btn_dfs = tk.Button(frame_algoritmos, bg="#27ae60", fg=COLOR_TEXTO_CLARO,
                          font=FUENTE_NORMAL, text="DFS", 
                          command=lambda: self._ejecutar_algoritmo('dfs'))
        btn_dfs.pack(side='left', padx=5)
        
        btn_dijkstra = tk.Button(frame_algoritmos, bg="#27ae60", fg=COLOR_TEXTO_CLARO,
                               font=FUENTE_NORMAL, text="Kruskal", 
                               command=lambda: self._ejecutar_algoritmo('dijkstra'))
        btn_dijkstra.pack(side='left', padx=5)

        btn_dijkstra = tk.Button(frame_algoritmos, bg="#27ae60", fg=COLOR_TEXTO_CLARO,
                               font=FUENTE_NORMAL, text="Kruskal", 
                               command=lambda: self._ejecutar_algoritmo('Prim'))
        btn_dijkstra.pack(side='left', padx=5)
        
    
        self.frame_grafico = ttk.Frame(main_frame)
        self.frame_grafico.pack(pady=10, fill='both', expand=True)
        
        self.lbl_grafico_vacio = tk.Label(self.frame_grafico, bg=COLOR_FONDO, fg=COLOR_TEXTO,
                                         font=FUENTE_NORMAL,
                                         text="No hay grafo para visualizar.\nCrea un grafo en la pestaña 'Crear Grafo'")
        self.lbl_grafico_vacio.pack(expand=True)
        
        self.canvas = None
        self.figura_actual = None

    def _procesar_enunciado(self):
        """Procesa el enunciado y crea el grafo"""
        enunciado = self.texto_enunciado.get(1.0, tk.END).strip()
        
        if not enunciado:
            messagebox.showwarning("Advertencia", "Por favor, escribe un enunciado.")
            return
        
        try:
            grafo = self.procesador.procesar_enunciado(enunciado)
            self.controlador.grafo_actual = grafo
            self._actualizar_info_grafo()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar: {str(e)}")
    
    def _actualizar_info_grafo(self):
        """Actualiza la información del grafo en la interfaz"""
        if self.controlador.grafo_actual:
            grafo = self.controlador.grafo_actual
            info = f"Tipo: {'Grafo'}\n"
            info += f"Vértices: {len(grafo.vertices)}\n"
            info += f"Aristas: {len(grafo.aristas)}"
            self.lbl_info.config(text=info)
            messagebox.showinfo("Éxito", "Grafo creado exitosamente!")
        else:
            self.lbl_info.config(text="No hay grafo creado")
    
    def _limpiar_enunciado(self):
        """Limpia el área de texto"""
        self.texto_enunciado.delete(1.0, tk.END)
    
    
    def _visualizar_grafo(self):
        """Visualiza el grafo actual"""
        if not self.controlador.grafo_actual:
            messagebox.showwarning("Advertencia", "No hay grafo para visualizar.")
            return
        
        try:
            for widget in self.frame_grafico.winfo_children():
                widget.destroy()
            
            self.visualizador = Visualizador()
            layout = self.combo_layout.get()
            self.visualizador.dibujar_grafo(self.controlador.grafo_actual, layout=layout)
            
            self.canvas = FigureCanvasTkAgg(self.visualizador.fig, master=self.frame_grafico)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill='both', expand=True)
            
            self.figura_actual = self.visualizador.fig
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al visualizar: {str(e)}")
    
    def _guardar_imagen(self):
        """Guarda la imagen del grafo"""
        if not self.figura_actual:
            messagebox.showwarning("Advertencia", "No hay gráfico para guardar.")
            return
        
        try:
            self.visualizador.guardar_imagen("grafo_generado.png")
            messagebox.showinfo("Éxito", "Imagen guardada como 'grafo_generado.png'")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
    
    def _ejecutar_algoritmo(self, algoritmo):
        """Ejecuta un algoritmo sobre el grafo actual"""
        if not self.controlador.grafo_actual:
            messagebox.showwarning("Advertencia", "No hay grafo para ejecutar algoritmos.")
            return
        
        try:
            if self.controlador.grafo_actual.vertices:
                primer_vertice = list(self.controlador.grafo_actual.vertices.keys())[0]
                resultado = self.controlador.ejecutar_algoritmo(algoritmo, inicio=primer_vertice)
                
                if resultado:
                    messagebox.showinfo(f"Resultado {algoritmo.upper()}", 
                                      f"Resultado: {resultado}")
                else:
                    messagebox.showwarning("Algoritmo", 
                                         f"No se pudo ejecutar {algoritmo}")
            else:
                messagebox.showwarning("Algoritmo", "El grafo no tiene vértices")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar {algoritmo}: {str(e)}")