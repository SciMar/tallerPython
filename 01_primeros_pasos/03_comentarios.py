"""
Tema: Comentarios en Python
Conceptos clave: comentario de línea (#), docstrings (comillas triples)
Error común de estudiantes: creer que las comillas triples son
"comentarios multilínea" — en realidad son strings de documentación.
"""

# Esta es una línea de comentario: Python la ignora por completo
print("Hola mundo")  # Comentario al final de una instrucción

# El numeral (#) se usa para comentarios de una sola línea.
# Para "comentar" varias líneas, se usa # al inicio de cada una
# (en VS Code: seleccionar las líneas y presionar Ctrl + K, Ctrl + C).


def saludar():
    """
    Esto es un DOCSTRING, no un comentario.
    Documenta funciones, clases y módulos.
    Python lo guarda: se puede leer con help(saludar).
    """
    print("Hola")


saludar()
help(saludar)  # Muestra el docstring en la terminal