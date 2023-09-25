"""
Este módulo contiene la clase que representa el juego de Conecta Cuatro,
incluyendo la lógica para manejar el tablero y verificar el estado del juego.
"""
class ConectaCuatro:
    """
    Representa el juego de Conecta Cuatro. 
    Contiene la lógica para manejar el tablero, verificar el estado del juego y cambiar de jugador.
    """
    VACIO = ' '
    JUGADOR_X = 'X'
    JUGADOR_O = 'O'
    FILAS = 6
    COLUMNAS = 7

    def __init__(self):
        self.tablero = [[self.VACIO for _ in range(self.COLUMNAS)] for _ in range(self.FILAS)]
        self.jugador_actual = self.JUGADOR_X

    def colocar_ficha(self, columna):
        """Coloca una ficha en la columna seleccionada."""
        if columna < 0 or columna >= self.COLUMNAS:
            raise ValueError(f"Columna inválida: {columna}. Debe ser entre 0 y {self.COLUMNAS - 1}")
        for fila in range(self.FILAS-1, -1, -1):
            if self.tablero[fila][columna] == self.VACIO:
                self.tablero[fila][columna] = self.jugador_actual
                return fila
        return -1

    def quitar_ficha(self, fila, columna):
        """Quita una ficha del tablero."""
        self.tablero[fila][columna] = self.VACIO

    def verificar_ganador(self):
        """Verifica si hay un ganador en el tablero actual."""
        for fila in range(self.FILAS):
            for columna in range(self.COLUMNAS):
                if self.tablero[fila][columna] == self.VACIO:
                    continue
                if self.es_linea(fila, columna) or self.es_diagonal(fila, columna):
                    return self.jugador_actual
        return None

    def es_linea(self, fila, columna):
        """Verifica si hay una línea de cuatro en horizontal o vertical desde la posición dada."""
        if columna + 3 < self.COLUMNAS and all(
            self.tablero[fila][columna + i] == self.jugador_actual for i in range(4)):
            return True
        if fila + 3 < self.FILAS and all(
            self.tablero[fila + i][columna] == self.jugador_actual for i in range(4)):
            return True
        return False

    def es_diagonal(self, fila, columna):
        """Verifica si hay una diagonal de cuatro desde la posición dada."""
        if columna + 3 < self.COLUMNAS and fila + 3 < self.FILAS and all(
            self.tablero[fila + i][columna + i] == self.jugador_actual for i in range(4)):
            return True
        if columna + 3 < self.COLUMNAS and fila - 3 >= 0 and all(
            self.tablero[fila - i][columna + i] == self.jugador_actual for i in range(4)):
            return True
        return False

    def esta_lleno(self):
        """Verifica si el tablero está lleno."""
        return all(self.tablero[0][columna] != self.VACIO for columna in range(self.COLUMNAS))

    def cambiar_jugador(self):
        """Cambia el jugador actual."""
        if self.jugador_actual == self.JUGADOR_X:
            self.jugador_actual = self.JUGADOR_O
        else:
            self.jugador_actual = self.JUGADOR_X
