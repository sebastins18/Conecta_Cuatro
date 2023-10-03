class IA:
    """
    Clase IA: Representa la inteligencia artificial para el juego.
    """
    VACIO = ' '
    JUGADOR_MAX = 'O'  # Suponiendo que 'O' es el jugador IA
    JUGADOR_MIN = 'X'

    def __init__(self, profundidad, algoritmo='AlphaBetaMinimax'):
        self.profundidad = profundidad
        self.algoritmo = algoritmo  # 'Minimax', 'AlphaBeta', o 'AlphaBetaMinimax'
        if self.profundidad < 1:
            raise ValueError("La profundidad debe ser un número entero positivo")

    def minimax(self, juego, profundidad, alpha, beta, jugador_maximizador):
        """
        Función principal del algoritmo minimax con poda alpha-beta.
        """
        print(f"Ejecutando minimax: profundidad={profundidad}, jugador_maximizador={jugador_maximizador}")
        ganador = juego.verificar_ganador()
        if ganador or juego.esta_lleno() or profundidad == 0:
            return self.evaluar_tablero(ganador)

        if jugador_maximizador:
            return self.maximizar(juego, profundidad, alpha, beta, jugador_maximizador, poda=self.algoritmo != 'Minimax')
        return self.minimizar(juego, profundidad, alpha, beta, jugador_maximizador, poda=self.algoritmo != 'Minimax')

    def evaluar_tablero(self, ganador):
        """
        Evalúa el tablero y retorna el valor.
        """
        print(f"Evaluando tablero: ganador={ganador}")
        if ganador == self.JUGADOR_MAX:
            return 1
        if ganador == self.JUGADOR_MIN:
            return -1
        return 0

    def maximizar(self, juego, profundidad, alpha, beta, jugador_maximizador, poda=True):
        print(f"Maximizando: profundidad={profundidad}, alpha={alpha}, beta={beta}, poda={poda}")
        eval_max = float('-inf')
        for col in range(7):
            if juego.tablero[0][col] == self.VACIO:
                fila = juego.colocar_ficha(col)
                juego.cambiar_jugador()
                eval_result = self.minimax(juego, profundidad - 1, alpha, beta, not jugador_maximizador)
                juego.quitar_ficha(fila, col)
                juego.cambiar_jugador()
                eval_max = max(eval_max, eval_result)
                if poda:
                    alpha = max(alpha, eval_result)
                    if beta <= alpha:
                        break
        return eval_max

    def minimizar(self, juego, profundidad, alpha, beta, jugador_maximizador, poda=True):
        print(f"Minimizando: profundidad={profundidad}, alpha={alpha}, beta={beta}, poda={poda}")
        eval_min = float('inf')
        for col in range(7):
            if juego.tablero[0][col] == self.VACIO:
                fila = juego.colocar_ficha(col)
                juego.cambiar_jugador()
                eval_result = self.minimax(juego, profundidad - 1, alpha, beta, not jugador_maximizador)
                juego.quitar_ficha(fila, col)
                juego.cambiar_jugador()
                eval_min = min(eval_min, eval_result)
                if poda:
                    beta = min(beta, eval_result)
                    if beta <= alpha:
                        break
        return eval_min

    def encontrar_mejor_movimiento(self, juego):
        print(f"Buscando el mejor movimiento: algoritmo={self.algoritmo}")
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
