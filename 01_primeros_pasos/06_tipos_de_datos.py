"""
Tema: Tipos de datos en Python
Conceptos clave: str, int, float, complex, list, tuple, set, dict, bool.
La función type() revela el tipo de cualquier valor.
Error común de estudiantes: confundir {1, 2, 3} (set) con [1, 2, 3] (lista).
"""

# ============ STRINGS (str) ============
comillas_simples = 'Simples'
comillas_dobles = "Dobles"
comillas_triples = '''Triples (permiten
varias líneas)'''

print(comillas_simples, type(comillas_simples))

# ============ NÚMEROS ============
entero = 1            # int
decimal = 3.14        # float
complejo = 5 + 2j     # complex (se usa en matemáticas/ingeniería)

print(entero, type(entero))
print(decimal, type(decimal))
print(complejo, type(complejo))

# ============ COLECCIONES: la clave está en el símbolo ============

# LISTA → corchetes [] — ordenada, permite duplicados, mutable
lista = [1, 2, 3, 4, 5]
print(lista, type(lista))
print(lista[0])  # acceso por índice: 1

# TUPLA → paréntesis () — ordenada, INMUTABLE
tupla = ("a", "b", "c")
print(tupla, type(tupla))

# SET → llaves {} — sin orden, SIN duplicados
conjunto = {1, 2, 3, 3, 3}
print(conjunto, type(conjunto))  # {1, 2, 3} ¡los duplicados desaparecen!

# DICCIONARIO → llaves {} pero con pares clave: valor
diccionario = {
    "nombre": "Ari",
    "edad": 34,
    "ciudad": "México"
}
print(diccionario, type(diccionario))
print(diccionario["nombre"])  # acceso por clave: Ari

# ============ BOOLEANOS (bool) ============
booleano_verdadero = True
booleano_falso = False
print(booleano_verdadero, type(booleano_verdadero))