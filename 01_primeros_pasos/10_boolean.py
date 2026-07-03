"""
Tema: Booleanos (bool)
Conceptos clave: True/False, comparaciones, truthy/falsy,
bool(), isinstance().
Error común de estudiantes: escribir true/false en minúscula
(en Python van con mayúscula inicial: True, False).
"""

# ============ VALORES BOOLEANOS ============
v = True
f = False
print(v)
print(f)
print(type(v))  # <class 'bool'>

# true = True   # ❌ NameError: en Python es True, con mayúscula

# ============ COMPARACIONES: producen booleanos ============
print(10 < 50)   # True  — 10 sí es menor que 50
print(50 < 10)   # False — 50 no es menor que 10
print(10 == 10)  # True  — igualdad se pregunta con == (no con =)
print(10 != 50)  # True  — "distinto de"

# ============ TRUTHY y FALSY ============
# Todo valor en Python puede evaluarse como booleano con bool().
# "Con contenido" → True (truthy). "Vacío o nulo" → False (falsy).

# TRUTHY (dan True):
print(bool("hola"))                    # string con contenido
print(bool("verdadero"))               # cualquier texto no vacío
print(bool(456))                       # cualquier número distinto de 0
print(bool(-1))                        # ¡los negativos también son truthy!
print(bool(["Pan", "Pizza", "Pera"]))  # lista con elementos

# FALSY (dan False) — son poquitos, vale la pena memorizarlos:
print(bool(""))      # string vacío
print(bool(0))       # el cero
print(bool([]))      # lista vacía
print(bool(None))    # el valor nulo

# ============ isinstance(): verificar el tipo ============
j = 10
print(isinstance(j, int))      # True — j es un entero

k = 5.7
print(isinstance(k, complex))  # False — k es float, no complex
print(isinstance(k, float))    # True
