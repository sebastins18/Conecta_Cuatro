"""
Este módulo contiene las clases que representan a los jugadores en el juego de Conecta 4, 
tanto humanos como computadoras.
"""
# pylint: disable=too-few-public-methods
class Jugador:
    """
    Representa un jugador en el juego. 
    Puede ser utilizado para representar tanto a jugadores humanos como a la computadora.
    """
    def __init__(self, simbolo):
        if simbolo not in ['X', 'O']:
            raise ValueError("El símbolo del jugador debe ser 'X' o 'O'")
        self.simbolo = simbolo  # 'X' o 'O'

    def obtener_simbolo(self):
        """Retorna el símbolo del jugador."""
        return self.simbolo


class Computadora(Jugador):
    """
    Representa una computadora en el juego.
    Utiliza un objeto de IA para realizar movimientos.
    """
    def __init__(self, simbolo, ia_instance):
        super().__init__(simbolo)
        if not hasattr(ia_instance  , 'encontrar_mejor_movimiento'):
            raise ValueError("El argumento 'ia' debe tener un método 'encontrar_mejor_movimiento'")
        self.ia_instance = ia_instance

    def realizar_movimiento(self, juego):
        """Hace un movimiento utilizando la IA."""
        columna = self.ia_instance.encontrar_mejor_movimiento(juego)
        juego.colocar_ficha(columna)
