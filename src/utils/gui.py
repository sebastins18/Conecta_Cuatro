"""
Módulo para representar la interfaz gráfica del juego Conecta Cuatro.
"""
import tkinter as tk
from tkinter import messagebox
from src.game import ConectaCuatro
from src.ai import IA
from src.player import Jugador, Computadora

# pylint: disable=too-many-instance-attributes
class ConectaCuatroGUI:
    """Clase para representar la interfaz gráfica del juego Conecta Cuatro."""
    def __init__(self, root):
        self.root = root
        self.root.title("Conecta Cuatro")

        self.juego = None
        self.humano = None
        self.ia_instance = None
        self.computadora = None


        self.opciones_frame = tk.Frame(root)
        self.opciones_frame.pack(side="top", pady=20)

        self.var_dificultad = tk.IntVar(value=1)
        self.dificultad = tk.Scale(self.opciones_frame, from_=1, to=10, orient='horizontal',
                                   length=300, sliderlength=30, label='Dificultad',
                                   variable=self.var_dificultad)
        self.dificultad.pack()

        self.var_dificultad.trace_add('write', self.cambiar_color_dificultad)

        self.boton_iniciar = tk.Button(
            self.opciones_frame,text="Iniciar Juego",command=self.iniciar_juego)
        self.boton_iniciar.pack(pady=20)


        self.juego_frame = tk.Frame(root)

        self.tiempo = 0
        self.cronometro_label = tk.Label(self.juego_frame, text="Tiempo: 0s")
        self.cronometro_label.pack(side="top")

        self.turno_label = tk.Label(self.juego_frame, text="Turno: Jugador")
        self.turno_label.pack(side="top")

        self.num_turnos = 0
        self.turnos_label = tk.Label(self.juego_frame, text="Turnos: 0")
        self.turnos_label.pack(side="top")

        self.canvas = tk.Canvas(self.juego_frame, width=700, height=670, bg='blue')
        self.canvas.pack(side="bottom")

        self.centrar_ventana()

    def cambiar_color_dificultad(self, *args):
        """Cambia el color del slider de dificultad según su valor."""
        valor = self.var_dificultad.get()
        if valor <= 3:
            color = 'green'
        elif valor <= 7:
            color = 'orange'
        else:
            color = 'red'

        self.dificultad.configure(troughcolor=color)

    def centrar_ventana(self, width=None, height=None):
        """
        Centra la ventana en la pantalla.
        
        :param width: Ancho de la ventana.
        :param height: Altura de la ventana.
        """
        if width and height:
            self.root.geometry(f"{width}x{height}")
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_pos  = (screen_width // 2) - (window_width // 2)
        y_pos  = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

    def iniciar_juego(self):
        """
        Inicia un nuevo juego ocultando las opciones y mostrando el tablero de juego.
        Configura la profundidad de la IA basándose en la dificultad seleccionada y
        prepara el entorno del juego para un nuevo juego, incluyendo la asignación de
        jugadores y la inicialización de variables de tiempo y turno. También se 
        encarga de dibujar el tablero inicial y de centrar la ventana.
        """
        self.opciones_frame.pack_forget()
        self.juego_frame.pack(fill="both", expand=True)
        self.centrar_ventana(700, 670)

        profundidad = self.dificultad.get()
        self.juego = ConectaCuatro()
        self.humano = Jugador('X')
        self.ia_instance   = IA(profundidad)
        self.computadora = Computadora('O', self.ia_instance  )

        self.root.bind("<Button-1>", self.movimiento_humano)

        self.tiempo = 0
        self.num_turnos = 0
        self.actualizar_cronometro()
        self.actualizar_turno()

        self.dibujar_tablero()
        self.centrar_ventana()

    def reiniciar_juego(self):
        """
        Reinicia el juego ocultando el tablero de juego y mostrando las opciones.
        Desvincula el evento de clic del botón, reinicia las variables de tiempo y
        turno
        """
        self.juego_frame.pack_forget()
        self.opciones_frame.pack(side="top", pady=20)
        self.centrar_ventana(300, 200)
        self.root.unbind("<Button-1>")
        self.tiempo = 0
        self.num_turnos = 0
        self.centrar_ventana()

    def actualizar_cronometro(self):
        """
        Actualiza el cronómetro del juego cada segundo, incrementando la variable de
        tiempo y reconfigurando la etiqueta del cronómetro con el nuevo valor.
        Programa la siguiente actualización para que ocurra después de 1 segundo (1000 ms).
        """
        self.cronometro_label.config(text=f"Tiempo: {self.tiempo}s")
        self.tiempo += 1
        self.juego_frame.after(1000, self.actualizar_cronometro)

    def actualizar_turno(self):
        """
        Actualiza la información del turno actual en la interfaz de usuario, mostrando
        si es el turno del Jugador o de la Computadora, y actualiza la etiqueta de
        turnos con el número actual de turnos.
        """
        jugador_actual = "Jugador" if self.juego.jugador_actual == 'X' else "Computadora"
        self.turno_label.config(text=f"Turno: {jugador_actual}")
        self.turnos_label.config(text=f"Turnos: {self.num_turnos}")

    def dibujar_tablero(self):
        """Dibuja el tablero en el canvas."""
        for fila in range(6):
            for columna in range(7):
                x_pos = columna * 100
                y_pos = fila * 100
                valor_celda = self.juego.tablero[fila][columna]
                if valor_celda == 'X':
                    color = 'red'
                elif valor_celda == 'O':
                    color = 'yellow'
                else:
                    color = 'white'
                self.canvas.create_oval(
                    x_pos, y_pos, x_pos + 100, y_pos + 100, fill=color, outline='blue')



    def movimiento_humano(self, evento):
        """Maneja el evento de clic del mouse en el canvas."""
        columna = evento.x // 100
        if self.juego.colocar_ficha(columna) == -1:
            messagebox.showinfo("Movimiento Inválido", "¡Columna llena!")
            return

        ganador = self.juego.verificar_ganador()
        if ganador or self.juego.esta_lleno():
            self.finalizar_juego(ganador)
            return

        self.num_turnos += 1
        self.juego.cambiar_jugador()
        self.actualizar_turno()
        self.dibujar_tablero()

        self.juego_frame.after(1000, self.movimiento_computadora)



    def movimiento_computadora(self):
        """Maneja el movimiento de la computadora."""
        columna = self.computadora.ia_instance .encontrar_mejor_movimiento(self.juego)
        self.juego.colocar_ficha(columna)
        ganador = self.juego.verificar_ganador()
        if ganador or self.juego.esta_lleno():
            self.finalizar_juego(ganador)
            return

        self.num_turnos += 1
        self.juego.cambiar_jugador()
        self.actualizar_turno()
        self.dibujar_tablero()

    def finalizar_juego(self, ganador):
        """Finaliza el juego y muestra un mensaje con el resultado."""
        self.dibujar_tablero()
        tiempo_jugado = f"Tiempo Jugado: {self.tiempo}s"
        turnos_jugados = f"Turnos Jugados: {self.num_turnos}"
        if ganador:
            mensaje = (f"¡{ganador} gana!\n{tiempo_jugado}\n{turnos_jugados}"
                    "\n¿Te gustaría jugar de nuevo?")
        else:
            mensaje = (f"¡Es un empate!\n{tiempo_jugado}\n{turnos_jugados}"
                    "\n¿Te gustaría jugar de nuevo?")
        respuesta = messagebox.askquestion("Fin del Juego", mensaje)

        if respuesta == 'yes':
            self.reiniciar_juego()
        else:
            self.root.quit()
