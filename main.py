"""
Este módulo contiene la función principal que inicia la aplicación.
"""
import tkinter as tk
from src.utils.gui import ConectaCuatroGUI

def main():
    """
    Inicia la aplicación creando una instancia de Tk y una de ConectaCuatroGUI,
    y luego entra en el bucle principal de eventos.
    """
    root = tk.Tk()
    ConectaCuatroGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
