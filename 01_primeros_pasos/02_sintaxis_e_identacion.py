"""
Tema: Sintaxis e indentación en Python
Conceptos clave: dos puntos (:), bloques de código, indentación (4 espacios)
Regla práctica: cada nuevo bloque aumenta un nivel de indentación.
Error común de estudiantes: olvidar indentar después de ":" 
o mezclar tabs con espacios.
"""

# ✅ CORRECTO: después de ":" el bloque va indentado
if 5 > 3:
    print("Cinco es mayor que tres")

# ❌ INCORRECTO: sin indentación Python lanza un error
# (descomentar para ver el error en clase)
# if 5 > 3:
# print("Cinco es mayor que tres")
#
# IndentationError: expected an indented block after 'if' statement

# Bloques anidados: cada if abre un nuevo nivel
if 5 > 3:
    print("Cinco es mayor que tres")      # nivel 1: dentro del if externo
    if 4 > 3:
        print("Cuatro es mayor que tres")  # nivel 2: dentro del if interno

print("Esto se ejecuta siempre")  # nivel 0: FUERA de los if



