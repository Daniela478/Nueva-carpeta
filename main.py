import tkinter as tk
from interfaz.ventana_principal import VentanaPrincipal
from grafo.algoritmos import AlgoritmosGrafos

def main():
    """Función principal que inicia la aplicación"""
    try:
        root = tk.Tk()
        root.title("Proyectito de Estructuras Discreta 2")
        
        app = VentanaPrincipal(root)

        AlgoritmosGrafos
        
        root.geometry("800x600")
        
        root.eval('tk::PlaceWindow . center')
        
        root.mainloop()
        
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()