import tkinter as tk
from interfaz.ventana_principal import VentanaPrincipal

def main():
    """Función principal que inicia la aplicación"""
    try:
        # Crear ventana principal
        aplicacion_grafos_principal = tk.Tk()
        aplicacion_grafos_principal.title("Proyectito de Estructuras Discreta 2")
        
        # Crear la aplicación
        app = VentanaPrincipal(aplicacion_grafos_principal)
        
        # Centrar la ventana
        aplicacion_grafos_principal.eval('tk::PlaceWindow . center')
        
        # Iniciar el loop principal
        aplicacion_grafos_principal.mainloop()
        
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()