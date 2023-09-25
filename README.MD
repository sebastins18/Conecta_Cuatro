# 🎮 Conecta Cuatro en Tkinter

## 🌟 [Descripción](#descripción)

Este proyecto implementa el clásico juego "Conecta Cuatro" 🟡🔴 utilizando Python 🐍 y la librería Tkinter para construir una interfaz gráfica 🖥️ interactiva y amigable. El juego permite a dos jugadores 🕹️ competir para conectar cuatro de sus fichas de forma consecutiva, horizontal, vertical o diagonalmente, antes que el oponente.


## 🎲 [Reglas del Juego](#reglas-del-juego)
- Los jugadores deben alternarse para soltar fichas en las columnas del tablero.
- Una ficha ocupará el espacio más bajo disponible en la columna seleccionada.
- El jugador que logre conectar cuatro de sus fichas en línea horizontal, vertical o diagonal, será el ganador 🏆.
- En caso de que el tablero se llene completamente y ningún jugador haya logrado conectar cuatro fichas, la partida será declarada empate 🤝.

## 🧠 [Estrategias de Juego](#estrategias-de-juego)
- **Ocupar el Centro:** 🎯 Dominar el centro del tablero permite tener más oportunidades de conectar cuatro fichas.
- **Bloquear al Adversario:** 🚫 Es crucial impedir que el oponente conecte cuatro fichas, sobre todo cuando ha alineado ya tres de ellas.
- **Doble Amenaza:** 💡 Generar oportunidades donde se pueda ganar de dos maneras distintas puede forzar errores del oponente.

## 💻 [Desarrollo e Implementación](#desarrollo-e-implementación)
### [Interfaz Gráfica](#interfaz-gráfica)
Tkinter proporciona una interfaz visual intuitiva y de fácil uso, permitiendo interacciones claras y visuales con el tablero de juego.

### [Jugadores](#jugadores)
El juego admite dos jugadores que pueden ser humanos 🙎‍♂️ o ser controlados por la inteligencia artificial 🤖 integrada en el juego.

### [Inteligencia Artificial](#inteligencia-artificial)
La inteligencia artificial utiliza algoritmos de búsqueda, como Minimax y poda Alpha-Beta, para evaluar el tablero y tomar las decisiones más optimizadas.

## 🔧 [Instalación y Configuración del Entorno Conda](#instalación-y-configuración-del-entorno-conda)

Sigue los siguientes pasos para configurar el entorno y ejecutar el juego:

1. **Clona el repositorio:**
    ```bash
    git clone https://github.com/sebastins18/Conecta_Cuatro.git
    ```

2. **Cambia al directorio del proyecto:**
    ```bash
    cd conecta-cuatro-gui
    ```

3. **Crea un ambiente conda:**
    ```bash
    conda create --name conecta-cuatro python=3.x
    ```

4. **Activa el ambiente conda:**
    ```bash
    conda activate conecta-cuatro
    ```

5. **Ejecuta el programa principal:**
    ```bash
    python main.py
    ```

## 🌟 [Características](#características)

- **Interfaz Amigable:** 👍 Diseño intuitivo y fácil de usar.
- **Desafiante IA:** 🧠 Compita contra una inteligencia artificial desafiante y ajustable.
- **Niveles de Dificultad:** 🌶️ Opta por diferentes niveles de dificultad según tu experiencia.
- **Contador de Tiempo y Turnos:** ⏲️ Monitorea el tiempo y los turnos con facilidad.
- **Ventana Ajustable:** 🖥️ Ajusta el tamaño de la ventana según tus preferencias.
- **Opción de Reinicio:** 🔄 Reinicia fácilmente el juego después de cada partida.

## 🎮 [Uso](#uso)

1. **Selecciona Nivel de Dificultad:** 🌶️ Elige la dificultad de la IA al iniciar el juego.
2. **Iniciar Juego:** 🎲 Comienza tu partida pulsando el botón "Iniciar Juego".
3. **Haz tu Movimiento:** 🕹️ Los jugadores seleccionan alternadamente la columna donde desean soltar su ficha.
4. **Fin de la Partida:** 🏁 Un mensaje declarará al ganador 🏆 y ofrecerá opciones para reiniciar el juego o salir.

## 👨‍💻 [Desarrolladores](#desarrolladores)

- [Sebastian Long Segura Méndez](mailto:sebastins08@gmail.com)
- [Mauren Miranda Quesada](mailto:otro_correo@example.com)

## 🔗 [Enlace del Proyecto](#enlace-del-proyecto)

[Conecta Cuatro en Tkinter](https://github.com/sebastins18/Conecta_Cuatro.git)

## 🤔 [Consideraciones de Profundidad](#consideraciones-de-profundidad)

### ¿Qué pasa cuando la profundidad se disminuye?

Al disminuir la profundidad de búsqueda de los algoritmos:
- **Eficiencia:** Los algoritmos serán más rápidos ya que explorarán menos nodos del árbol de juego.
- **Calidad de la Jugada:** Las jugadas podrían ser menos óptimas, ya que se considerarán menos posibilidades futuras.

### ¿Qué pasa cuando la profundidad aumenta?

Al aumentar la profundidad de búsqueda de los algoritmos:
- **Eficiencia:** Los algoritmos serán más lentos y consumirán más recursos, ya que explorarán más nodos del árbol de juego.
- **Calidad de la Jugada:** Las jugadas serán más óptimas y estratégicas, al considerar más posibilidades y consecuencias futuras de cada movimiento.

### Conclucion

Al ajustar la profundidad de los algoritmos de búsqueda como Minimax y poda Alpha-Beta, se debe encontrar un equilibrio entre la eficiencia en tiempo y recursos y la calidad de las decisiones tomadas por la inteligencia artificial. Un nivel de profundidad demasiado bajo resultará en decisiones apresuradas y posiblemente subóptimas, mientras que un nivel de profundidad demasiado alto puede ser computacionalmente costoso y, en algunos casos, innecesario.
