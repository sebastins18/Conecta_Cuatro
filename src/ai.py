"""
Módulo IA: Contiene la clase IA para el juego.
"""
class IA:
    """
    Clase IA: Representa la inteligencia artificial para el juego.
    """
    VACIO = ' '
    JUGADOR_MAX = 'O'  # Suponiendo que 'O' es el jugador IA
    JUGADOR_MIN = 'X'

    def __init__(self, profundidad):
        self.profundidad = profundidad
        if self.profundidad < 1:
            raise ValueError("La profundidad debe ser un número entero positivo")

    # pylint: disable=too-many-arguments
    def minimax(self, juego, profundidad, alpha, beta, jugador_maximizador):
        """
        Función principal del algoritmo minimax con poda alpha-beta.
        """
        ganador = juego.verificar_ganador()
        if ganador or juego.esta_lleno() or profundidad == 0:
            return self.evaluar_tablero(ganador)

        if jugador_maximizador:
            return self.maximizar(juego, profundidad, alpha, beta)
        return self.minimizar(juego, profundidad, alpha, beta)

    def evaluar_tablero(self, ganador):
        """
        Evalúa el tablero y retorna el valor.
        """
        if ganador == self.JUGADOR_MAX:
            return 1
        if ganador == self.JUGADOR_MIN:
            return -1
        return 0

    def maximizar(self, juego, profundidad, alpha, beta):
        """
        Encuentra el valor máximo entre los hijos del estado actual.
        """
        eval_max = float('-inf')
        for col in range(7):
            if juego.tablero[0][col] == self.VACIO:
                fila = juego.colocar_ficha(col)
                juego.cambiar_jugador()
                eval_result = self.minimax(juego, profundidad - 1, alpha, beta, False)
                juego.quitar_ficha(fila, col)
                juego.cambiar_jugador()
                eval_max = max(eval_max, eval_result)
                alpha = max(alpha, eval_result)
                if beta <= alpha:
                    break
        return eval_max

    def minimizar(self, juego, profundidad, alpha, beta):
        """
        Encuentra el valor mínimo entre los hijos del estado actual.
        """
        eval_min = float('inf')
        for col in range(7):
            if juego.tablero[0][col] == self.VACIO:
                fila = juego.colocar_ficha(col)
                juego.cambiar_jugador()
                eval_result = self.minimax(juego, profundidad - 1, alpha, beta, True)
                juego.quitar_ficha(fila, col)
                juego.cambiar_jugador()
                eval_min = min(eval_min, eval_result)
                beta = min(beta, eval_result)
                if beta <= alpha:
                    break
        return eval_min

    def encontrar_mejor_movimiento(self, juego):
        """
        Encuentra y retorna el mejor movimiento posible.
        """
        mejor_movimiento = -1
        mejor_valor = float('-inf')
        for col in range(7):
            if juego.tablero[0][col] == self.VACIO:
                fila = juego.colocar_ficha(col)
                juego.cambiar_jugador()
                valor_movimiento = self.minimax(
                    juego, self.profundidad - 1, float('-inf'), float('inf'), False)
                juego.quitar_ficha(fila, col)
                juego.cambiar_jugador()
                if valor_movimiento > mejor_valor:
                    mejor_movimiento = col
                    mejor_valor = valor_movimiento
        return mejor_movimiento
